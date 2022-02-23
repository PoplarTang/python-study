"""
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if
that character appears only once in the original string, or ")" if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.
"""
import codewars_test as Test


def duplicate_encode(word):
    lower_word = word.lower()
    print(lower_word, "---------------")
    data_dict = {}
    rst = []
    for b in list(lower_word):
        if b not in data_dict:
            data_dict[b] = 0
        data_dict[b] += 1

    for b in list(lower_word):
        if data_dict[b] > 1:
            rst.append(")")
        else:
            rst.append("(")

    return ''.join(rst)


if __name__ == '__main__':
    Test.assert_equals(duplicate_encode("din"), "(((")
    Test.assert_equals(duplicate_encode("recede"), "()()()")
    Test.assert_equals(duplicate_encode("Success"), ")())())", "should ignore case")
    Test.assert_equals(duplicate_encode("(( @"), "))((")
