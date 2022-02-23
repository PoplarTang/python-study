"""
https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
"""

import codewars_test as test
import math

def is_square(n):
    return n >= 0 and (n**0.5).is_integer()
    # return n > -1 and math.sqrt(n) % 1 == 0

test.describe("is_square")
test.it("should work for some examples")
test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
test.assert_equals(is_square( 0), True, "0 is a square number")
test.assert_equals(is_square( 3), False, "3 is not a square number")
test.assert_equals(is_square( 4), True, "4 is a square number")
test.assert_equals(is_square(25), True, "25 is a square number")
test.assert_equals(is_square(26), False, "26 is not a square number")