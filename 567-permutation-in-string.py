class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for x in s1:
            d[x] = d.get(x, 0) + 1
        
        start = 0
        for end, x in enumerate(s2):
            if x in d:
                d[x] -= 1
                if not d[x]:    d.pop(x)
                if not d:       return True

            else:
                while start < end and s2[start] != x:
                    d[s2[start]] = d.get(s2[start], 0) + 1
                    start += 1
                
                start = start + 1
        
        return False



