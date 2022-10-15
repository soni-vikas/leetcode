from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]

        count = 1
        for i in range(int(n / 2)):
            for col in range(i, n - 1):
                res[i][col] = count
                count += 1

            for row in range(i, n - 1):
                res[row][n - 1] = count
                count += 1

            for col in range(n - 1, i, -1):
                res[n - 1][col] = count
                count += 1

            for row in range(n - 1, i, -1):
                res[row][i] = count
                count += 1

            i += 1
            n -= 1

        if len(res) % 2: res[int(len(res) / 2)][int(len(res) / 2)] = count
        return res
