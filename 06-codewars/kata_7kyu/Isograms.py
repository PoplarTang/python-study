"""
https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
"""
import codewars_test as Test
from collections import Counter


def is_isogram(string):
    return string == "" or max(Counter(string.lower()).values()) < 2

# is_isogram = lambda s: len(set(s.lower())) == len(s)

Test.assert_equals(is_isogram("Dermatoglyphics"), True )
Test.assert_equals(is_isogram("isogram"), True )
Test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
Test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
Test.assert_equals(is_isogram("isIsogram"), False )
Test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )