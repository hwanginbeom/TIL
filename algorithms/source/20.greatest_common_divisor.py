def greatest_common_divisor(a,b):
    if a < b:
        min = a
    else:
        min = b

    gcd = 0

    for i in range(1, min+1):
        if a % i == 0:
            if b % i == 0:
                gcd = i

    return gcd


def greatest_common_divisor2(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1


# 유클리드
def greatest_common_divisor3(a, b):
    if b == 0:           # 종료 조건
        return a

    return greatest_common_divisor3(b, a % b)  # 좀 더 작은 값으로 자기 자신을 호출


# 피보나치 수열
def fibonacci1(n):
    if n < 2:
        return 2
    return fibonacci1(n-1) + fibonacci1(n-2)


print(greatest_common_divisor(100, 200))
print(greatest_common_divisor2(100, 200))
print(greatest_common_divisor3(200, 100))
print(fibonacci1(5))
