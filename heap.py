"""Max Heap implemented using an array"""
from __future__ import annotations
__author__ = "Brendon Taylor, modified by Jackson Goerner"
__docformat__ = 'reStructuredText'

from typing import Generic
from referential_array import ArrayR, T


class MaxHeap(Generic[T]):
    MIN_CAPACITY = 1

    def __init__(self, max_size: int, an_array: ArrayR[T] = None) -> None:
        """
        Initialise the MaxHeap.

        Complexity
        - Worst case: O(N log (N)), where N is the maximum size of the array or the length of an_array, whichever
                      is larger, when an_array is provided
        - Best case: O(N), where N is the maximum size of the array, when an_array is not provided

        """
        self.length = 0
        self.the_array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)  # O(N)

        if an_array is not None:

            self.length = len(an_array)
            # copy an_array to self.the_array (shift by 1)
            for i in range(self.length):  # O(N)
                self.the_array[i + 1] = an_array[i]
            # heapify every parent
            for i in range(max_size // 2, 0, -1):  # O(N)
                self.sink(i)  # O(log (N))

    def __len__(self) -> int:
        return self.length

    def clear(self) -> None:
        """Clears the heap"""
        self.length = 0

    def is_full(self) -> bool:
        return self.length + 1 == len(self.the_array)

    def rise(self, k: int) -> None:
        """
        Rise element at index k to its correct position
        :pre: 1 <= k <= self.length
        """
        item = self.the_array[k]
        while k > 1 and item > self.the_array[k // 2]:
            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        self.the_array[k] = item

    def add(self, element: T) -> bool:
        """
        Swaps elements while rising
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = element
        self.rise(self.length)

    def largest_child(self, k: int) -> int:
        """
        Returns the index of k's child with greatest value.
        :pre: 1 <= k <= self.length // 2
        """
        
        if 2 * k == self.length or \
                self.the_array[2 * k] > self.the_array[2 * k + 1]:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:
        """ Make the element at index k sink to the correct position.
            :pre: 1 <= k <= self.length
            :complexity: ???
        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            max_child = self.largest_child(k)
            if self.the_array[max_child] <= item:
                break
            self.the_array[k] = self.the_array[max_child]
            k = max_child

        self.the_array[k] = item
        
    def get_max(self) -> T:
        """ Remove (and return) the maximum element from the heap. """
        if self.length == 0:
            raise IndexError

        max_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)
        return max_elt


if __name__ == '__main__':
    items = [int(x) for x in input('Enter a list of numbers: ').strip().split()]
    heap = MaxHeap(len(items))

    for item in items:
        heap.add(item)
        
    while len(heap) > 0:
        print(heap.get_max())
