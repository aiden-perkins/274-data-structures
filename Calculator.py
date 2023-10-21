import numpy as np
import ArrayStack
import ChainedHashTable
import re
import BinaryTree
import operator
"""
"""


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable()

    def set_variable(self, k: object, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()
        for char in s:
            if char == '(':
                stack.push('(')
            elif char == ')':
                if stack.size() < 1:
                    return False
                stack.pop()
        return True if stack.size() == 0 else False

    def _build_parse_tree(self, exp: str) -> BinaryTree:
        if not self.matched_expression(exp):
            raise ValueError
        split_exp = re.findall('[-+*/()]|\w+|\W+', exp)
        t = BinaryTree.BinaryTree()
        t.r = BinaryTree.BinaryTree.Node()
        current = t.r
        for char in split_exp:
            if char == '(':
                current = current.insert_left(BinaryTree.BinaryTree.Node())
            elif char in ['+', '-', '*', '/']:
                current.set_key(char)
                current.set_val(char)
                current = current.insert_right(BinaryTree.BinaryTree.Node())
            elif char.isalnum():
                current.set_key(char)
                current.set_val(self.dict.find(char))
                current = current.parent
            elif char == ')':
                current = current.parent
        return t

    def _evaluate(self, root: BinaryTree.BinaryTree.Node):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        left_val = self.dict.find(root.left.k) if root.left.k not in op else self._evaluate(root.left)
        right_val = self.dict.find(root.right.k) if root.right.k not in op else self._evaluate(root.right)
        if left_val is None or right_val is None:
            raise ValueError
        return op[root.v](left_val, right_val)

    def evaluate(self, exp):
        print(f'Evaluating expression: {self.print_expression(exp)}')
        return self._evaluate(self._build_parse_tree(exp).r)

    def print_expression(self, ex):
        variables = [x for x in re.split('\W+', ex) if x.isalnum()]
        everything_else = re.split('\w+', ex)
        s = ''
        for i in range(max(len(variables), len(everything_else)) - 1):
            s += everything_else[i]
            variable = self.dict.find(variables[i])
            s += str(variable) if variable is not None else str(variables[i])
        s += everything_else[max(len(variables), len(everything_else)) - 1]
        return s
