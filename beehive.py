from dataclasses import dataclass
from heap import MaxHeap


@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    def __lt__(self, other):
        self_emerald = min(self.capacity, self.volume) * self.nutrient_factor
        other_emerald = min(other.capacity, other.volume) * other.nutrient_factor

        return self_emerald < other_emerald

    def __ge__(self, other):
        self_emerald = min(self.capacity, self.volume) * self.nutrient_factor
        other_emerald = min(other.capacity, other.volume) * other.nutrient_factor

        return self_emerald >= other_emerald


class BeehiveSelector:
    def __init__(self, max_beehives: int):
        """
        Initialise the BeehiveSelector.

        Complexity
        - Worst case: O(1), initialisation operation is a constant time operation.
        - Best case: O(1), same as worst case

        """
        self.heap = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        """
        Replace all current (possibly none) beehives in the selector with the beehives in the list
        provided as an argument.

        Complexity
        - Worst case: O(M), where M is len(hive_list).
        - Best case: O(M), same as worst case

        """
        self.heap.clear()  # O(1)

        for hive in hive_list:  # O(M)
            self.heap.add(hive)

    def add_beehive(self, hive: Beehive):
        """
        Complexity
        - Worst case: O(log(N)), where N is the number of beehives in the selector.
        - Best case: O(log(N)), same as worst case

        """
        self.heap.add(hive)  # O(log(N)

    def harvest_best_beehive(self) -> Beehive:
        """
        Complexity
        - Worst case: O(log(N)), where N is the number of beehives in the selector.
        - Best case: O(log(N)), same as worst case

        """
        # Get the beehive with maximum honey yield from the heap
        best_hive = self.heap.get_max()  # O(log(N))

        new_hive = Beehive(best_hive.x, best_hive.y, best_hive.z, best_hive.capacity, best_hive.nutrient_factor,
                           best_hive.volume - best_hive.capacity)
        self.add_beehive(new_hive)

        best_emerald = min(best_hive.capacity, best_hive.volume) * best_hive.nutrient_factor

        return best_emerald  # Return the harvested beehive
