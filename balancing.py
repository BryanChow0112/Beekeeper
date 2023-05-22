from __future__ import annotations

from ratio import Percentiles
from threedeebeetree import Point, BeeNode
from math import floor


def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    """
    complexity: O(N * log(N)) where N is the number of element in input list
    """
    res = []

    def make_ordering_inner(my_list):
        if len(my_list) <= 17:
            res.extend(my_list)
            return
        else:
            a = 12.5

            p_x = Percentiles()
            p_y = Percentiles()
            p_z = Percentiles()

            for point in my_list:
                p_x.add_point(point[0])  # O(log(N))
                p_y.add_point(point[1])
                p_z.add_point(point[2])

            res_x = p_x.ratio(a, a)
            res_y = p_y.ratio(a, a)  # O(log(N) + O)
            res_z = p_z.ratio(a, a)

            current_point = None

            for point in my_coordinate_list:
                if point[0] in res_x and point[1] in res_y and point[2] in res_z:
                    current_point = point
                    res.append(point)
                    my_list.remove(point)  # O(log(N))
                    break

            octant1 = []
            octant2 = []
            octant3 = []
            octant4 = []
            octant5 = []
            octant6 = []
            octant7 = []
            octant8 = []

            for point in my_list:
                if point[0] < current_point[0]:
                    if point[1] < current_point[1]:
                        if point[2] < current_point[2]:
                            octant1.append(point)
                        else:
                            octant2.append(point)
                    else:
                        if point[2] < current_point[2]:
                            octant3.append(point)
                        else:
                            octant4.append(point)
                else:
                    if point[1] < current_point[1]:
                        if point[2] < current_point[2]:
                            octant5.append(point)
                        else:
                            octant6.append(point)
                    else:
                        if point[2] < current_point[2]:
                            octant7.append(point)
                        else:
                            octant8.append(point)

            make_ordering_inner(octant1)
            make_ordering_inner(octant2)
            make_ordering_inner(octant3)
            make_ordering_inner(octant4)
            make_ordering_inner(octant5)
            make_ordering_inner(octant6)
            make_ordering_inner(octant7)
            make_ordering_inner(octant8)

    make_ordering_inner(my_coordinate_list)
    return res

if __name__ == "__main__":
    my_coordinate_list = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (2, 3, 1),
            (5, 6, 4),
            (8, 9, 7),
        ]
    print(make_ordering(my_coordinate_list))
