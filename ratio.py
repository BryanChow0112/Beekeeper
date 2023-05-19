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
        Computes a list of all items fitting the larger than/smaller than criteria.
        O(log(N) + O), where O is the number of points returned by the function.
        """
        res = []
        smaller = ceil(x / 100 * len(self.bst))
        larger = len(self.bst) - ceil(y / 100 * len(self.bst))

        if smaller != 0:
            smaller = self.bst.kth_smallest(smaller, self.bst.root).key
        if larger != 0:
            larger = self.bst.kth_smallest(larger, self.bst.root).key

        # Traverse the binary search tree and store the items within the desired range
        def collect_items_in_range(current, start_rank, end_rank, result):
            """
            Collects the items in the range [start_rank, end_rank] using in-order traversal.
            Appends the items to the result list.
            """
            if current is None:
                return

            # In-order traversal
            if start_rank < current.key:
                collect_items_in_range(current.left, start_rank, end_rank, result)
            if start_rank < current.key <= end_rank:
                result.append(current.key)
            if current.key < end_rank:
                collect_items_in_range(current.right, start_rank, end_rank, result)

        collect_items_in_range(self.bst.root, smaller, larger, res)
        print(res)
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
