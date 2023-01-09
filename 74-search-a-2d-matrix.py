from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = binary_search(matrix, target,
                            exit_condition=lambda ls, target, low, high, mid: ls[mid][0] <= target <= ls[mid][-1],
                            target_less_than_mid_value=lambda ls, target, low, high, mid: target < ls[mid][0]
                            )
        col = binary_search(matrix[row], target,
                            exit_condition=lambda ls, target, low, high, mid: target == ls[mid],
                            target_less_than_mid_value=lambda ls, target, low, high, mid: target < ls[mid]
                            )

        return matrix[row][col] == target


def binary_search(ls, target, exit_condition, target_less_than_mid_value):
    n = len(ls)
    low, high = 0, n - 1
    while low < high:
        mid = int(high - (high - low) / 2)
        if exit_condition(ls, target, low, high, mid):
            return mid

        if target_less_than_mid_value(ls, target, low, high, mid):
            high = mid - 1
        else:
            low = mid + 1

    return low
