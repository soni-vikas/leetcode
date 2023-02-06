import math
from typing import List

MIN = -1000001
MAX = +1000001


class Solution:
    def findMedianSortedArrays(self, y: List[int], x: List[int]) -> float:
        if len(y) < len(x):
            y, x = x, y

        n_1 = len(y)
        n_2 = len(x)

        l = (n_1 + n_2)

        left, right = 0, len(x) - 1

        def get_val(ls, i):
            if i == -1: return MIN
            if i == len(ls): return MAX
            return ls[i]

        while True:
            xi = math.floor(right - (right - left) / 2)
            yi = int(l / 2) - (xi + 1) - 1

            x1 = get_val(x, xi)
            x2 = get_val(x, xi + 1)

            y1 = get_val(y, yi)
            y2 = get_val(y, yi + 1)
            
            if x1 <= y2 and y1 <= x2:
                max_val = max(x1, y1)
                min_val = min(x2, y2)
                if l % 2:
                    return min_val

                else:
                    return (max_val + min_val) / 2

            elif x1 > y2:
                right = xi - 1

            else:
                left = xi + 1


if __name__ == '__main__':

    s = Solution()
    ls = [
        ([10, 20, 30, 40, 50, 60], [15, 25, 35, 45, 55, 65]),
        ([], [15, 25, 35, 45, 55, 65]),
        ([10, 30, 40, 70], [20, 35, 90, 100, 110]),
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
        ([2, 3, 4, 5], [6, 7]),
        ([2, 3, 4, 5], [0, 1]),
        ([3], [-2, -1]),
        ([5], [4])
    ]

    for a, b in ls:
        c = sorted([*a, *b])
        print(c)
        a = s.findMedianSortedArrays(a, b)
        e = (c[math.floor((len(c) - 1) / 2)] + c[math.ceil((len(c) - 1) / 2)]) / 2
        print("median is ", a, e, a == e)
