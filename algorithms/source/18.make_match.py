def find_same_name(a):
    n = len(a)
    count = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] != a[j]:
                print(a[i] + "-" + a[j])
                count += 1
    return count


name = ["Tom", "Jerry", "Mike"] # 대소문자 유의: 파이썬은 대소문자를 구분함

print(find_same_name(name))

