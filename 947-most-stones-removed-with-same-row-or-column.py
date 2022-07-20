from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # create graph
        rows = {}
        cols = {}
        for r, c in stones:
            rows[r] = rows.get(r, [])
            rows[r].append((r, c))

            cols[c] = cols.get(c, [])
            cols[c].append((r, c))

        visited = set()

        # finding all possible island in graph
        res = 0
        for r, c in stones:
            if (r, c) not in visited:
                res += 1
                self.dfs(r, c, rows, cols, visited)

        return len(stones) - res

    def dfs(self, r, c, rows, cols, visited):
        if (r, c) in visited:
            return

        visited.add((r, c))
        for i, j in rows[r]:
            self.dfs(i, j, rows, cols, visited)

        for i, j in cols[c]:
            self.dfs(i, j, rows, cols, visited)
