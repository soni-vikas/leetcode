from typing import List


class Solution:
    def xor(cls, a):
        _xor = 0
        for i in a: _xor ^= i
        return _xor

    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        1. take the xor of all elements in the nums:
        2. if x & y are unique in the list then xor would be x ^ y.
        3. create two group where msb of x^y is set & where msb is not set.
            for e.g. xor of [1, 2, 1, 2, 3, 5] => 6 or (110 in binary).
            take the number from xor where only msb is set i.e. "100" or 4 in binary
                group with msb set (i.e. for e in nums: e | 4) => [5]
                group with msb set  => [1, 2, 1, 2, 3]

        4. take the xor of each set individually & return. [5, 3]
        """
        _xor = self.xor(nums)
        _sum = 0
        _val = 1

        while abs(_xor) // 2:
            _val <<= 1
            _xor //= 2

        a = 0
        b = 0
        for num in nums:
            if num | _val == num:
                a ^= num
            else:
                b ^= num

        return [a, b]


if __name__ == '__main__':
    for i in [
        [-1, 0],
        [1, 2, 1, 2, 3, 5]
    ]:
        print(Solution().singleNumber(i))
