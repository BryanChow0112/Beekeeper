from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]


@dataclass
class BeeNode:
    key: Point
    item: I
    subtree_size: int = 1
    octant1: BeeNode | None = None #(<<<)
    octant2: BeeNode | None = None #(<<>=)
    octant3: BeeNode | None = None #(<>=<)
    octant4: BeeNode | None = None #(<>=>=)
    octant5: BeeNode | None = None #(>=<<)
    octant6: BeeNode | None = None #(>=<>=)
    octant7: BeeNode | None = None #(>=>=<)
    octant8: BeeNode | None = None #(>=>=>=)

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        if point[0] < self.key[0]:
            if point[1] < self.key[1]:
                if point[2] < self.key[2]:
                    if self.octant1 is not None:
                        return self.octant1
                else:
                    if self.octant2 is not None:
                        return self.octant2
            else:
                if point[2] < self.key[2]:
                    if self.octant3 is not None:
                        return self.octant3
                else:
                    if self.octant4 is not None:
                        return self.octant4
        else:
            if point[1] < self.key[1]:
                if point[2] < self.key[2]:
                    if self.octant5 is not None:
                        return self.octant5
                else:
                    if self.octant6 is not None:
                        return self.octant6
            else:
                if point[2] < self.key[2]:
                    if self.octant7 is not None:
                        return self.octant7
                else:
                    if self.octant8 is not None:
                        return self.octant8
        return None




class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        def get_tree_node_by_key_aux(current: BeeNode, key: Point) -> BeeNode:
            if current is None:
                raise KeyError('Key not found: {0}'.format(key))
            elif key == current.key:
                return current
            elif key[0] < current.key[0]:
                if key[1] < current.key[1]:
                    if key[2] < current.key[2]:
                        return get_tree_node_by_key_aux(current.octant1, key)
                    else:
                        return get_tree_node_by_key_aux(current.octant2, key)
                else:
                    if key[2] < current.key[2]:
                        return get_tree_node_by_key_aux(current.octant3, key)
                    else:
                        return get_tree_node_by_key_aux(current.octant4, key)
            elif key[0] >= current.key[0]:
                if key[1] < current.key[1]:
                    if key[2] < current.key[2]:
                        return get_tree_node_by_key_aux(current.octant5, key)
                    else:
                        return get_tree_node_by_key_aux(current.octant6, key)
                else:
                    if key[2] < current.key[2]:
                        return get_tree_node_by_key_aux(current.octant7, key)
                    else:
                        return get_tree_node_by_key_aux(current.octant8, key)

        return get_tree_node_by_key_aux(self.root, key)

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
        Attempts to insert an item into the tree, using the Key to insert it
        """
        if current is None:  # Base case: at the leaf
            current = BeeNode(key, item)
            self.length += 1
        elif key[0] < current.key[0]:
            if key[1] < current.key[1]:
                if key[2] < current.key[2]:
                    current.octant1 = self.insert_aux(current.octant1, key, item)
                else:
                    current.octant2 = self.insert_aux(current.octant2, key, item)
            else:
                if key[2] < current.key[2]:
                    current.octant3 = self.insert_aux(current.octant3 , key, item)
                else:
                    current.octant4 = self.insert_aux(current.octant4, key, item)
            current.subtree_size += 1
        elif  key[0] >= current.key[0]:
            if key[1] < current.key[1]:
                if key[2] < current.key[2]:
                    current.octant5 = self.insert_aux(current.octant5, key, item)
                else:
                    current.octant6 = self.insert_aux(current.octant6, key, item)
            else:
                if key[2] < current.key[2]:
                    current.octant7 = self.insert_aux(current.octant7 , key, item)
                else:
                    current.octant8  = self.insert_aux(current.octant8 , key, item)
            current.subtree_size += 1
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')
        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        return current.octant1 is None and current.octant2 is None and current.octant3 is None and \
               current.octant4 is None and current.octant5 is None and current.octant6 is None and current.octant7 is \
               None and current.octant8 is None


if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size)  # 2
