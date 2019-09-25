
def solution1(number):
    """
    https://www.06-codewars.com/kata/multiples-of-3-or-5/solutions/python/me/best_practice
    """
    return sum(i for i in range(number) if i % 5 == 0 or i % 3 == 0 )

def getCount(inputStr):
    num_vowels = 0
    for s in inputStr:
        if s in 'aeiou':
            num_vowels += 1
    return num_vowels

def disemvowel1(string):
    return "".join(filter(lambda x: x not in "aeiouAEIOU", string))
def disemvowel(string):
    return string.translate(None,)


def duplicate_count(text):
    """ 已通过
    https://www.codewars.com/kata/counting-duplicates/train/python
    """
    arr = list(text.lower())
    counter = dict()
    for i in arr:
        counter[i] = counter.get(i, 0) + 1

    print(counter)
    rst = 0
    for value in counter.values():
        if value > 1:
            rst += 1
    return rst

if __name__ == '__main__':
    # print(solution1(10))
    # print(getCount("abracadabra"))
    # print(disemvowel("This website is for losers LOL!"))
    count = duplicate_count("indivisibility")
    print(count) # 1
    count = duplicate_count("aabBcde")
    print(count) # 2
