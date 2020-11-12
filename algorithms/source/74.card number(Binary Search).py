# 10816

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index


value = int(input())
array = list(map(int, input().split()))
array.sort()
value2 = int(input())
array2 = list(map(int, input().split()))

for i in array2:
    print(count_by_range(array, i, i), end=' ')