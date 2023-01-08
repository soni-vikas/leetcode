import math

MODULO_NUMBER = 1000000007


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (self.pow(5, math.ceil(n/2)) * self.pow(4, math.floor(n/2))) % MODULO_NUMBER

    def pow(self, x, y):
        if y == 0:
            return 1

        if y == 1:
            return x

        temp = self.pow(x, int(y / 2))
        return (temp * temp * (x if y % 2 else 1)) % MODULO_NUMBER
