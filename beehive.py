from dataclasses import dataclass
from heap import MaxHeap
from threedeebeetree import ThreeDeeBeeTree
from bst import BinarySearchTree
from referential_array import ArrayR
from balancing import make_ordering
@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

class BeehiveSelector:
    def __init__(self, max_beehives: int):
        self.heap = MaxHeap(max_beehives)
        self.tdbt = ThreeDeeBeeTree()
        self.bst = BinarySearchTree()

    def set_all_beehives(self, hive_list: list[Beehive]):
        """
        Complexity Expectation O(M), where M is len(hive_list)
        """
        """ use make_ordering??"""
        pass

    def add_beehive(self, hive: Beehive):
        """
        Complexity Expectation log(N), where N is the number of beehives in the selector
        """
        self.tdbt[(hive.x, hive.y, hive.z)] = hive  # Add the beehive to the 3D Bee Tree
        honey_yield = min(hive.capacity, hive.volume) * hive.nutrient_factor  # Calculate honey yield

        if honey_yield in self.bst:
            # If the honey yield already exists in the Binary Search Tree, append the beehive to the existing list
            self.bst[honey_yield].append(hive)
        else:
            # If the honey yield is new, create a list with the beehive as its single element
            self.bst[honey_yield] = [hive]

        self.heap.add(honey_yield)  # Add honey yield to the max heap

    def harvest_best_beehive(self) -> Beehive:
        """
        Complexity Expectation log(N), where N is the number of beehives in the selector
        """
        honey_yield = self.heap.get_max() # O(log(N)) # Get the maximum honey yield from the heap
        hive_list = self.bst[honey_yield] # O(log(N)) # Get the list of beehives with the maximum honey yield

        # Select the first beehive from the list
        hive = hive_list[0]
        del hive_list[0]  # Remove the harvested beehive from the list

        if len(hive_list) == 0:
            # If the list becomes empty, remove the honey yield from the Binary Search Tree
            del self.bst[honey_yield]

        self.tdbt[(hive.x, hive.y, hive.z)] = Beehive(hive.x, hive.y, hive.z, hive.capacity, hive.nutrient_factor, hive.volume - hive.capacity)

        new_hive = Beehive(hive.x, hive.y, hive.z, hive.capacity, hive.nutrient_factor, hive.volume - hive.capacity)
        self.add_beehive(new_hive)

        return honey_yield  # Return the harvested beehive


