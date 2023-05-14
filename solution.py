'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

1 <= nums.length <= 10**4
0 <= nums[i] <= 10**5
'''


class Solution:

    def canJump(self, nums: list[int]) -> bool:

        self._check_nums_len(nums)
        self._check_is_values_valid(nums)

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

    def _check_nums_len(self, nums):
        if (len(nums) < 1) or (len(nums) > 10**4):
            raise ValueError

    def _check_is_values_valid(self, nums):
        for i in nums:
            if type(i) != int:
                raise ValueError
            if (i < 0) or (i > 10**5):
                raise ValueError
