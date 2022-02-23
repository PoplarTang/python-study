"""
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python
"""

import codewars_test as test

def tickets(people):
    m_25 = m_50 = 0
    for person in people:
        if person == 25:
            m_25 += 1
        elif person == 50:
            m_25 -= 1
            m_50 += 1
        elif person == 100:
            if m_50 > 0:
                m_50 -= 1
                m_25 -= 1
            else:
                m_25 -= 3

        if m_25 < 0:
            return "NO"

    return "YES"


test.assert_equals(tickets([25, 25, 50]), "YES")
test.assert_equals(tickets([25, 100]), "NO")
