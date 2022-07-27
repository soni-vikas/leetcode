MAX_LEN = 10 ** 5 + 1


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = {}
        count = len(t)
        for ch in t:
            m[ch] = m.get(ch, 0)
            m[ch] += 1

        start = 0
        end = 0
        max_start = 0
        max_len = MAX_LEN

        n = len(s)
        while end < n:
            if s[end] in m:
                if m[s[end]] > 0:
                    count -= 1

                m[s[end]] -= 1

            end += 1
            while count == 0:
                if end - start < max_len:
                    max_start = start
                    max_len = min(end - start, max_len)

                if s[start] not in m:
                    start += 1
                else:
                    m[s[start]] += 1
                    if m[s[start]] > 0:
                        count += 1

                    start += 1

        if max_len == MAX_LEN:
            return ""

        return s[max_start:max_start + max_len]


if __name__ == '__main__':
    tc = [
        ["ADOBECODEBANC", "ABC"],
        ["a", "a"],
        ["a", "b"],
        ["abc", "b"],
        ["bba", "ab"],
        ["ab", "b"],
        ["bba", "ab"],
        ["aaaaaaaaaaaabbbbbcdd", "abcdd"]
    ]
    for t in tc:
        print(Solution().minWindow(t[0], t[1]))
