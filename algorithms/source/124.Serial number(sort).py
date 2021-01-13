# 1431 - 시리얼 번호
a = int(input())
array = []

for i in range(a):
    b = input()
    array.append(b)

# 1번조건
array.sort(key=len)

for i in range(0,len(array)-1):
    # 2번조건
    if len(array[i]) == len(array[i+1]):
        for z in range(i+1, len(array)):
            a = 0
            b = 0
            if len(array[i]) != len(array[z]):
                break
            for j in range(0,len(array[i])):
                if array[i][j].isdigit() == True:
                    a += int(array[i][j])
            for j in range(0,len(array[i])):
                if array[z][j].isdigit() == True:
                    b += int(array[z][j])
            if a > b :
                array[i], array[z] = array[z], array[i]
            # 3번조건
            elif b == a:
                for last in range(0,len(array[i])):
                    if array[i][last] > array[z][last]:
                        array[i], array[z] = array[z], array[i]
                        break
                    elif array[i][last] < array[z][last]:
                        break

for i in array:
    print(i)


# 선영

def serial_sum(x):
    sum = 0
    for i in x:
        if i.isnumeric():
            sum += int(i)
    return sum

n = int(input())
guitars = []
for _ in range(n):
    guitars.append(input())
guitars = sorted(guitars, key=lambda x: (len(x), serial_sum(x), x))

for i in guitars:
    print(i)

# 경현

n = int(input())
num_list = [[] for _ in range(n)]
number_list = [str(i) for i in range(1,10)]
num = 0

for i in range(n):
    zip = input().strip()
    for j in zip:
        num_list[i].extend(j)
        if j in number_list:
            num += int(j)
    num_list[i].extend([num])
    num = 0

num_list = sorted(num_list, key=lambda x:(len(x), x[-1], x[::1]))
for i in num_list:
    print(''.join(i[:-1]))