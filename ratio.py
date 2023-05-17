from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")


class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.bst = BinarySearchTree()

    def add_point(self, item: T):
        self.bst[item] = None

    def remove_point(self, item: T):
        del self.bst[item]

    def ratio(self, x, y):
        """
        Computes a list of all items fitting the larger than/smaller than criteria. This list doesn't need to be sorted.
        O(log(N)+O), where O is the number of points returned by the function.
        """
        res: list = []
        smaller: int = ceil(x / 100 * len(self.bst))
        larger: int = len(self.bst) - ceil(y / 100 * len(self.bst))
        for n in range(smaller, larger):
            res.append(self.bst.kth_smallest(n + 1, self.bst.root).key)
        return res


if __name__ == "__main__":
    points = list(range(50))
    import random

    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
