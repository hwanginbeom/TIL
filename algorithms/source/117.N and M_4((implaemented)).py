# 15651번 - N과 M(4)
n, m = map(int, input().split())

check = [False] * (n + 1)
a = [0] * m


def go(index, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
        return
    for i in range(1, n + 1):
        a[index] = i
        go(index + 1, n, m)



go(0, n, m)