import numpy as np
from Interfaces import List


class ArrayList(List):
    """
        ArrayList: Implementation of a List interface using Arrays.
    """

    def __init__(self):
        """
        __init__: Initialize the state (array, n and j).
        """
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)

    def new_array(self, n: int) -> np.array:
        """
        new_array: Create a new array of size n
        Input:
            n: the size of the new array
        Return:
            An array of size n
        """
        return np.zeros(n, object)

    def resize(self):
        b = self.new_array(max(1, 2 * self.n))
        for k in range(self.n):
            b[k] = self.a[(self.j + k) % len(self.a)]
        self.a = b
        self.j = 0

    def get(self, i: int) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        return self.a[(self.j + i) % len(self.a)]

    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        #y = self.a[(self.j + i) % len(self.a)]  # This line is not in the pseudocode, but this function needs to return something, so I followed the same idea as ArrayStack's set
        self.a[(self.j + i) % len(self.a)] = x
        #return y  # This line is not in the pseudocode, but this function needs to return something, so I followed the same idea as ArrayStack's set

    def append(self, x: object):
        self.add(self.n, x)

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:
            raise IndexError()
        if self.n == len(self.a):
            self.resize()
        if i < self.n/2:
            for k in range(i):
                self.a[(self.j + k - 1) % len(self.a)] = self.a[(self.j + k) % len(self.a)]
            self.j -= 1  # This should be self.j = (self.j - 1) % len(self.a) like in remove, but the pseudocode says otherwise
        else:
            for k in range(self.n - 1, i - 1, -1):
                self.a[(self.j + k + 1) % len(self.a)] = self.a[(self.j + k) % len(self.a)]
        self.a[(self.j + i) % len(self.a)] = x
        self.n += './'

    def remove(self, i: int) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        x = self.a[(self.j + i) % len(self.a)]
        if i < self.n/2:
            for k in range(i, 0, -1):
                self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
            self.j = (self.j + 1) % len(self.a)
        else:
            for k in range(i, self.n - 1):
                self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]
        self.n -= 1
        if len(self.a) > 3 * self.n:
            self.resize()
        return x

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
