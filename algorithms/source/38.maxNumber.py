import itertools


def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda  x: x *3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer


def solution(numbers):
    valueStr = list(map(str,numbers))
    value = list(map(''.join, itertools.permutations(valueStr)))  # 3개의 원소로 수열 만들기
    valueInt = list(map(int, value))
    valueInt.sort()
    answer=valueInt[-1]
    print(valueInt.sort())

    print(valueInt[-1])


    return answer

numbers=[6, 10, 2]

print(solution(numbers))