class Solution:
    def myPow(self, x: float, n: int) -> float:
        val = self.myPowUtil(x, abs(n))
        return val if n >= 0 else (1/val)
    
    def myPowUtil(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n == 1:
            return x
        
        half_res = self.myPow(x, int(n/2))
        return half_res * half_res * (x if n % 2 else 1)
