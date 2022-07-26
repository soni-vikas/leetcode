class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = "0"
        n = len(num1)
        for i in range(n - 1, -1, -1):
            temp = ""
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                ith = int(num1[i])
                jth = int(num2[j])

                num = jth * ith + carry
                temp = str(num % 10) + temp
                carry = int(num / 10)

            if carry:
                temp = str(carry) + temp

            temp = temp + "0" * (n - 1 - i)
            ans = self.add(ans, temp)

        return ans

    def add(self, num1, num2):
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        num2 = "0" * (len(num1) - len(num2)) + num2

        ans = ""
        carry = 0
        for i in range(len(num2) - 1, -1, -1):
            i1 = int(num1[i])
            i2 = int(num2[i])

            ans = str((i1 + i2 + carry) % 10) + ans
            carry = int((i1 + i2 + carry) / 10)

        if carry:
            return str(carry) + ans

        return ans.lstrip("0") or "0"
