class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0

        m = {}
        ans = 0

        for end, item in enumerate(s):
            m[item] = m.get(item, 0)
            m[item] += 1

            while (end - start + 1) - max(m.values() or [0]) > k:
                m[s[start]] -= 1
                start += 1

            ans = max(ans, end - start + 1)
            end += 1
        
        return ans

