class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphic_map = {}
        for i in range(len(s)):
            if s[i] not in isomorphic_map:
                if t[i] not in isomorphic_map.values():
                    isomorphic_map[s[i]] = t[i]

                else:
                    return False

            elif isomorphic_map[s[i]] != t[i]:
                return False

        return True
