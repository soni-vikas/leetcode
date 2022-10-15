class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1

        for i in t:
            if i not in d:
                return False
            
            d[i] -= 1
            if d[i] == 0:
                d.pop(i)
        
        if d: return False
        return True
