from typing import List

mem = {0: [1]}


class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex not in mem:
            previous = [0] + self.getRow(rowIndex - 1) + [0]
            mem[rowIndex] = []
            for i in range(1, len(previous)):
                mem[rowIndex].append(previous[i - 1] + previous[i])

        return mem[rowIndex]
