class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while r - l > 1:
            m = int(r - (r - l) / 2)
            square = m * m
            if square == x:
                return m
            elif square < x:
                l = m
            else:
                r = m

        if r * r <= x:
            return r

        return l
