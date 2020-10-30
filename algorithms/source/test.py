import sys
input = sys.stdin.readline

a, b = map(int, input().split())



def gcd(a, b):
    if b > 0:
        tmp = a % b
        a = b
        b = tmp
        gcd(a, b)
    else:
        return a


def lcm(a, b):
    a * b // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))
