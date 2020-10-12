def find_same_name(a):
    n = len(a)
    same_name = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                same_name.add(a[i])
    return same_name

v = ["Tom", "Jerry", "Mike", "Tom"]

name = ["Tom", "Jerry", "Mike", "Tom"] # 대소문자 유의: 파이썬은 대소문자를 구분함

print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]

print(find_same_name(name2))