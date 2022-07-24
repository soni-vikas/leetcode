class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        m = 1
        start = 0
        window = {s[0]}
        for i in range(1, len(s)):
            if s[i] in window:
                while s[start] != s[i]:
                    window.remove(s[start])
                    start += 1

                window.remove(s[start])
                start += 1

            window.add(s[i])
            m = max(m, i - start + 1)

        return m
