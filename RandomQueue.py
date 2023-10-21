import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        """
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        """
        
        if self.n < 1:
            raise IndexError()
        r = random.randint(0, self.n-1)
        x = self.a[(self.j + r) % len(self.a)]
        self.a[(self.j + r - 1) % len(self.a)] = super().remove()
        if len(self.a) > 3 * self.n:
            self.resize()
        return x
