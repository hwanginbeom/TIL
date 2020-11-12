# 1920
def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
     # 값을 찾은 경우 인덱스 반환
    if array[mid] == target:
        return 1 # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1) # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

value = int(input())
array = list(map(int, input().split()))
array.sort()
value2 = int(input())
array2 = list(map(int, input().split()))

for i in array2:
    result = binary_search(array,i,0,value-1)
    if result == None:
        print(result)
    else :
        print(result)
