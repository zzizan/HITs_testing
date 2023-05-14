from unittest import TestCase
from solution import Solution

class TestSolution(TestCase):
    def test_can_jump_with_true(self):
        sut = Solution()
        nums = [2, 3, 1, 1, 4]
        self.assertTrue(sut.canJump(nums))

    def test_can_jump_with_false(self):
        sut = Solution()
        nums = [3, 2, 1, 0, 4]
        self.assertFalse(sut.canJump(nums))

    '''1 <= nums.length <= 10^4'''

    def test_can_jump_with_valid_length_one(self):
        sut = Solution()
        nums = [3]
        self.assertTrue(sut.canJump(nums))

    def test_can_jump_with_valid_length_two(self):
        sut = Solution()
        nums = [3, 5]
        self.assertTrue(sut.canJump(nums))

    def test_can_jump_with_invalid_length_zero(self):
        sut = Solution()
        nums = []
        with self.assertRaises(ValueError):
            sut.canJump(nums)

    def test_can_jump_with_valid_length_max(self):
        sut = Solution()
        nums = [1] * (10**4)
        self.assertTrue(sut.canJump(nums))

    def test_can_jump_with_valid_length_max_minus_one(self):
        sut = Solution()
        nums = [1] * ((10**4) - 1)
        self.assertTrue(sut.canJump(nums))

    def test_can_jump_with_invalid_length_max_plus_one(self):
        sut = Solution()
        nums = [1] * ((10**4) + 1)
        with self.assertRaises(ValueError):
            sut.canJump(nums)

    '''0 <= nums[i] <= 10 ** 5'''

    def test_can_jump_with_valid_value_zero(self):
        sut = Solution()
        nums = [0]
        self.assertTrue(sut.canJump(nums))

    def test_can_jump_with_valid_value_one(self):
        sut = Solution()
        nums = [1]
        self.assertTrue(sut.canJump(nums))

    def test_can_jump_with_invalid_value_minus_one(self):
        sut = Solution()
        nums = [3, -1, 4]
        with self.assertRaises(ValueError):
            sut.canJump(nums)

    def test_can_jump_with_valid_value_max(self):
        sut = Solution()
        nums = [10**5]
        self.assertTrue(sut.canJump(nums))

    def test_can_jump_with_valid_value_max_minus_one(self):
        sut = Solution()
        nums = [(10**5) - 1]
        self.assertTrue(sut.canJump(nums))

    def test_can_jump_with_invalid_value_max_plus_one(self):
        sut = Solution()
        nums = [(10**5) + 1]
        with self.assertRaises(ValueError):
            sut.canJump(nums)

    def test_can_jump_with_invalid_string_value(self):
        sut = Solution()
        nums = [1, 'a', 2]
        with self.assertRaises(ValueError):
            sut.canJump(nums)

    def test_can_jump_with_invalid_float_value(self):
        sut = Solution()
        nums = [1, 1.5, 2]
        with self.assertRaises(ValueError):
            sut.canJump(nums)

    def test_can_jump_with_invalid_non_array_object(self):
        sut = Solution()
        nums = '1 15 2'
        with self.assertRaises(ValueError):
            sut.canJump(nums)
