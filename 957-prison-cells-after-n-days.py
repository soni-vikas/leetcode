from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        cells = self.update_cells(cells)
        n -= 1

        for i in range(n % 14):
            cells = self.update_cells(cells)

        return cells

    def update_cells(self, cells):
        new_cells = [0]
        for j in range(1, len(cells) - 1):
            new_cells.append(int(cells[j - 1] == cells[j + 1]))

        new_cells.append(0)
        return new_cells
