"""
https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
"""
import codewars_test as test

def unique_in_order(it):
    return [it[i] for i in range(len(it)) if i == 0 or (it[i - 1] != it[i])]

test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
