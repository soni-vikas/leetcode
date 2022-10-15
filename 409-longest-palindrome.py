class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s: d[i] = d.get(i, 0) + 1
        
        res = 0
        middle_char = False
        for v in d.values():
            if v >= 2:  res += int(v / 2) * 2
            if v % 2:   middle_char = True
        
        return res + middle_char
