# 2748 번
value = int(input())

d = [0 for _ in range(value+1)]

if value == 1:
    print(1)
elif value == 2:
    print(1)
else:
    d[1] = 1
    d[2] = 1

    for i in range(3, value+1):
        d[i] = d[i-1] + d[i-2]
    print(d[value])


ne_count[m]))