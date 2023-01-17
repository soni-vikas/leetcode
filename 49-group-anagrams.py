class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            d[s] = d.get(s, [])
            d[s].append(strs[i])
        
        return list(d.values())
