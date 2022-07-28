class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str, k: int = 2) -> int:
        m = {}
        res = end = start = 0

        while end < len(s):
            m[s[end]] = m.get(s[end], 0) + 1

            while len(m) > k:
                m[s[start]] -= 1
                if m[s[start]] == 0:
                    m.pop(s[start])

                start += 1

            res = max(res, sum(m.values()))
            end += 1

        return max(res, sum(m.values()))
