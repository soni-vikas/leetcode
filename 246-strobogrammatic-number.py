class Solution:
    strobogrammatic_map = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6",
    }

    def isStrobogrammatic(self, num: str) -> bool:
        i = 0
        j = len(num) - 1

        while i <= j:
            if self.strobogrammatic_map.get(num[i]) != num[j]:
                return False

            i += 1
            j -= 1

        return True
