"""
https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
"""
import codewars_test as Test

import math

def next_bigger(n):
    arr = []
    for i in range(len(str(n))):
        arr.append(n % 10)
        n = math.floor(n / 10)

    arr.sort()
    print(arr)

    return 21

Test.assert_equals(next_bigger(12), 21)
Test.assert_equals(next_bigger(513), 531)
Test.assert_equals(next_bigger(531), -1)
Test.assert_equals(next_bigger(2017), 2071)
Test.assert_equals(next_bigger(414), 441)
Test.assert_equals(next_bigger(144), 414)