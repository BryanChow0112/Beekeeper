from __future__ import annotations

from ratio import Percentiles
from threedeebeetree import Point, BeeNode
from math import floor


def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    res = []
    def make_ordering_inner(my_list):
        if len(my_list) <= 17:
            res.extend(my_list)
        else:
            n = len(my_list)
            pivot = floor((n + 7) / 8) / n

            p_x = Percentiles()
            for point in my_list:
                p_x.add_point(point[0])

            res_x = p_x.ratio(pivot, pivot)

            p_y = Percentiles()
            for point in my_list:
                p_y.add_point(point[1])

            res_y = p_y.ratio(pivot, pivot)

            p_z = Percentiles()
            for point in my_list:
                p_z.add_point(point[2])

            res_z = p_z.ratio(pivot, pivot)

            for point in my_coordinate_list:
                if point[0] in res_x and point[1] in res_y and point[2] in res_z:
                    res.append(point)
                    my_list.remove(point)
                    break

            mid = len(my_list)//2

            return make_ordering_inner(my_list[:mid])
            return make_ordering_inner(my_list[mid:])

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