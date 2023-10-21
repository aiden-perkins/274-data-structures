from typing import Any

from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i >= self.n:
            return self.dummy  # pseudocode says to return None here but codepost needs it to not be None, so it can get next/prev, and we can't raise an IndexError because again codepost needs it to return something
        if i < self.n/2:
            p = self.dummy.next
            for _ in range(i):
                p = p.next
        else:
            p = self.dummy
            for _ in range(self.n - i):
                p = p.prev
        return p

    def get(self, i) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        return self.get_node(i).x

    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w: Node, x: object) -> Node:
        if w is None:
            raise IndexError()  # pseudocode says to return Exception? can't return None, so I guess we raise an IndexError instead of returning it
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i: int, x: object) -> Node:
        if i < 0 or i > self.n:
            raise IndexError()
        return self.add_before(self.get_node(i), x)

    def _remove(self, w: Node) -> object:
        # we have no w = self.get_node(i) because remove(i) does that for us already
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        # runs in O(n/2) 😎 (yes I know O(n/2) is the same as O(n) but it looks cool ok?)
        left = self.dummy.next
        right = self.dummy.prev
        while left != right and left.prev != right:
            if not left.x.lower().isalpha():
                left = left.next
                continue
            if not right.x.lower().isalpha():
                right = right.prev
                continue
            if left.x.lower() != right.x.lower():
                return False
            left = left.next
            right = right.prev
        return True

    def reverse(self):
        head = self.dummy
        for _ in range(self.n + 1):
            tail = head.prev
            head.prev = head.next
            head.next = tail
            head = head.prev

    def __str__(self):
        s = ""
        u = self.dummy.next
        while u is not self.dummy:
            s += str(u.x)
            u = u.next
            if u is not None:
                s += ","
        return "[" + s[:-1] + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
