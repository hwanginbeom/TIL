import sys
from collections import Counter
value = int(sys.stdin.readline())
value_list = [0] * value
print(value)
number = []
for i in range(value):
    number.append(int(sys.stdin.readline()))


def function1(number):
    result = 0
    for i in number:
        result += i
    result = result / len(number)
    return round(result, 2)

def function2(number):
    result = len(number) // 2
    return number[result]

def function3(number):
    cnt = Counter(number)
    result = cnt.most_common(1)[0][0]
    return result


# def function2(number):
#     dict
#     result = len(number) // 2
#     return number[result]


print(function1(number))
print(function2(number))
print(function3(number))