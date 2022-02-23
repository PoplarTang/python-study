"""
https://www.codewars.com/kata/552c028c030765286c00007d/train/python
"""
import codewars_test as Test

def iq_test(numbers):
    nums = [int(x) % 2 for x in numbers.split(" ")]
    return nums.index(1) + 1 if nums.count(1) == 1 else nums.index(0) + 1


Test.assert_equals(iq_test("2 4 7 8 10"), 3)
Test.assert_equals(iq_test("1 2 2"), 1)

print(~~8)