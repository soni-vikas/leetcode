class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        s_len = len(s)
        p_len = len(p)
        while i < s_len and j < p_len:
            if j + 1 < p_len and p[j + 1] == "*":
                sub_pattern = p[j + 2:]
                while i < s_len and p[j] in [s[i], "."]:
                    if self.isMatch(s[i:], sub_pattern):
                        return True

                    i += 1

                return self.isMatch(s[i:], sub_pattern)

            if p[j] not in [s[i], "."]:
                return False

            i += 1
            j += 1

        while j + 1 < p_len:
            if p[j + 1] != "*":
                break
            j += 2

        if i == s_len and j == p_len:
            return True

        return False
