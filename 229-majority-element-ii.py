class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = 0
        e1 = e2 = None

        for i in nums:
            if e1 == i:
                c1 += 1

            elif e2 == i:
                c2 += 1

            elif c1 == 0:
                e1 = i
                c1 += 1

            elif c2 == 0:
                e2 = i
                c2 += 1

            else:
                c1 -= 1
                c2 -= 1

            # print("i=", i, ", e1=", e1, ", e2=", e2, ", c1=", c1, ", c2=", c2, sep="")

        print(e1, e2, c1, c2)
        count1 = count2 = 0
        for i in nums:
            if e1 == i:
                count1 += 1

            elif e2 == i:
                count2 += 1

        res = []
        if count1 > len(nums) / 3:
            res.append(e1)

        if count2 > len(nums) / 3:
            res.append(e2)

        return res
