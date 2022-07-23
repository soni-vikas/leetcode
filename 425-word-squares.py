from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        words = list(set(words))

        n = len(words)
        m = len(words[0])
        ans = []
        wordMap = {}
        for w in words:
            wordMap[w[0]] = wordMap.get(w[0], [])
            wordMap[w[0]].append(w)

        for w in words:
            self.wordSquaresUtil(wordMap, [w], m, ans)

        return ans

    def wordSquaresUtil(self, wordMap, matrix, m, ans):
        n = len(matrix)
        if n == m:
            ans.append([*matrix])
            return

        for w in wordMap.get(matrix[0][n], []):
            matrix.append(w)
            if self.check(matrix):
                self.wordSquaresUtil(wordMap, matrix, m, ans)

            matrix.pop()

        return

    def check(self, matrix):
        n = len(matrix)

        for i in range(1, n - 1):
            if matrix[n - 1][i] != matrix[i][n - 1]:
                return False

        return True
