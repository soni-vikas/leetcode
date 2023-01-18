alpha_numeric = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        s = s.lower()
        while i < j:
            while s[i] not in alpha_numeric:
                i+=1
                if i>=j: return True

            while s[j] not in alpha_numeric:
                j-=1
                if i>=j: return True

            if s[i] != s[j]:
                return False
            
            i+=1
            j-=1

        return True
            
