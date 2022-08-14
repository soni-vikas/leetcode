class Solution:
    def clean(self, s, i) -> int:
        while i >= 0:
            if s[i] != "#":
                return i

            hash_count = 0
            while i >= 0:
                if s[i] == "#":
                    hash_count += 1
                else:
                    hash_count -= 1

                i -= 1
                if hash_count == 0:
                    break

        return i

    def backspaceCompare(self, s: str, t: str) -> bool:
        i = self.clean(s, len(s) - 1)
        j = self.clean(t, len(t) - 1)

        while i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False

            i = self.clean(s, i - 1)
            j = self.clean(t, j - 1)

        return i == -1 and j == -1