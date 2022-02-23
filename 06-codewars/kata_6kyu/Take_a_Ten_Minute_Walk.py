"""
https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

"""
import codewars_test as test

def is_valid_walk2(walk):

    if len(walk) != 10:
        return False

    pos = [0, 0]
    for i in walk:
        if i == 'n':
            pos[1] += 1
        elif i == 's':
            pos[1] -= 1
        elif i == 'e':
            pos[0] += 1
        elif i == 'w':
            pos[0] -= 1

    return pos[0] == 0 and pos[1] == 0

from collections import Counter

def is_valid_walk(walk):
    if len(walk) != 10: return False
    c = Counter(walk)
    return c['n'] == c['s'] and c['w'] == c['e']


#some test cases for you...
test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True')
test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False')
test.expect(not is_valid_walk(['w']), 'should return False')
test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False')