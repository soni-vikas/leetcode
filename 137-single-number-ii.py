from typing import List


class Solution:
    @classmethod
    def to_binary(cls, num):
        b = ""
        while num:
            b = str(num % 2) + b
            num = int(num / 2)

        return b

    @classmethod
    def to_decimal(cls, b):
        d = 0
        for i in b:
            d = d * 2 + int(i)

        return d

    def singleNumber(self, nums: List[int]) -> int:
        """
        1. represent each number as binary equivalent.
        2. add numbers bitwise in an array.
        3. for e.g. nums = [5, 5, 12, 5]
                5 => 0 1 0 1
                5 => 0 1 0 1
                8 => 1 1 0 0
                5 => 0 1 0 1
        4. bitwise sum => [1, 4, 0, 3]
        5. take modulus of each number => [1, 1, 0, 0]
        6. return the decimal equivalent of the array => 12
        """

        k = 3
        res = [0] * 32
        neg_number_count = 0
        for num in nums:
            b = self.to_binary(num)
            neg_number_count = (neg_number_count + int(num < 0)) % k

            for i, e in enumerate(b):
                res[i - len(b)] = (res[i - len(b)] + int(e)) % 3

        return -self.to_decimal(res) if neg_number_count else self.to_decimal(res)
