class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        double the input array like nums + nums
        run the stack method on this array.
        :param nums:
        :return:
        """
        n = len(nums)
        next_greater = [-1] * n

        stack = []
        for i in range(n * 2):
            i = i % n
            while stack and nums[stack[-1]] < nums[i]:
                next_greater[stack.pop()] = nums[i]

            stack.append(i)

        return next_greater

    def nextGreaterElements_method_2(self, nums: List[int]) -> List[int]:
        """
        finding index of maximum element.
        loop over _max, _max + len(nums) + 1 & use stack method.
        :param nums:
        :return:
        """

        _max = -1
        for i in range(len(nums)):
            if _max == -1:
                _max = i
            elif nums[_max] < nums[i]:
                _max = i

        next_greator = [0] * len(nums)

        stack = []
        for i in range(_max, _max + len(nums) + 1):
            i = i % len(nums)
            while stack and nums[stack[-1]] < nums[i]:
                next_greator[stack.pop()] = nums[i]

            stack.append(i)

        for i in stack:
            next_greator[i] = -1

        return next_greator
