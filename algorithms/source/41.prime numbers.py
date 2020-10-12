import itertools
import math
from itertools import permutations

def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False
    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    pool = []
    a=[]
    for i in numbers:
        pool.append(i)
    for i in range(0,len(numbers)):
        c=list(map(''.join, itertools.permutations(pool, len(numbers)-i)))
        for i in c:
            if check(int(i)) ==True:
                a.append(i)
    a=list(map(int,a))
    answer = len(set(a))
    print(a)
    return answer


numbers="011"
print(solution(numbers))



def solution3(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)