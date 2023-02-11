from typing import List

revert = lambda x: "1" if x == "0" else "0"


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        take revert the ith item from ith nums. finally append all the number.  
        :param nums: 
        :return: 
        """
        output = ""
        for idx, num in enumerate(nums):
            output += revert(num[idx])

        return output
