class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1
