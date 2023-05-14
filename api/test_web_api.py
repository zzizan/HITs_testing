import pytest
from lib.req import *

class TestClass:
    def test_get_form_http_status(self):
        assert get_form().status_code == 200

    def test_post_form_http_status(self):
        nums = "2 3 1 1 4"
        assert post_form(nums).status_code == 200

    def test_can_jump_with_true(self):
        nums = "2 3 1 1 4"
        assert post_form(nums).text == 'True'

    def test_can_jump_with_false(self):
        nums = "3 2 1 0 4"
        assert post_form(nums).text == 'False'

    def test_can_jump_with_valid_length_one(self):
        nums = "3"
        assert post_form(nums).status_code == 200

    def test_can_jump_with_valid_length_two(self):
        nums = "3 5"
        assert post_form(nums).status_code == 200

    def test_can_jump_with_invalid_length_zero(self):
        nums = ""
        assert post_form(nums).status_code == 400

    def test_can_jump_with_valid_length_max(self):
        nums = "1 " * (10**4)
        assert post_form(nums).status_code == 200

    def test_can_jump_with_valid_length_max_minus_one(self):
        nums = "1 " * ((10**4) - 1)
        assert post_form(nums).status_code == 200

    def test_can_jump_with_invalid_length_max_plus_one(self):
        nums = "1 " * ((10**4) + 1)
        assert post_form(nums).status_code == 400

    def test_can_jump_with_valid_value_zero(self):
        nums = "0"
        assert post_form(nums).status_code == 200

    def test_can_jump_with_valid_value_one(self):
        nums = "1"
        assert post_form(nums).status_code == 200

    def test_can_jump_with_invalid_value_minus_one(self):
        nums = "3 -1 4"
        assert post_form(nums).status_code == 400

    def test_can_jump_with_valid_value_max(self):
        nums = 10 ** 5
        assert post_form(nums).status_code == 200

    def test_can_jump_with_valid_value_max_minus_one(self):
        nums = (10 ** 5) - 1
        assert post_form(nums).status_code == 200

    def test_can_jump_with_invalid_value_max_plus_one(self):
        nums = (10 ** 5) + 1
        assert post_form(nums).status_code == 400

    def test_can_jump_with_invalid_string_value(self):
        nums = "1 a 2"
        assert post_form(nums).status_code == 400

    def test_can_jump_with_invalid_float_value(self):
        nums = "1 1.5 2"
        assert post_form(nums).status_code == 400


