# 2839
value = int(input())

count = value // 5
box = 0

while(1):
    if count == -1:
        box = -1
        break
    if count == 0:
        if value % 3 == 0:
            box = value//3
            break
        else:
            box = -1
            break
    elif (value - (count*5)) % 3 == 0:
        count2 = (value - (count * 5)) // 3
        box = count + count2
        break
    else:
        count = count-1

print(box)