def sort_up(a):
    sort_Value = a
    sortList = []
    while len(a) > 0:
        sortList.append(min(a))
        sort_Value.remove(min(a))
    return sortList

def sort_down(a):
    sort_Value = a
    sortList = []
    while len(a) > 0:
        sortList.append(max(a))
        sort_Value.remove(max(a))
    return sortList

def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1): # 0부터 n -2까지 반복
        # i번 위치부터 끝까지 자료 값 중 최솟값의 위치를 찾음
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # 찾은 최솟값을 i번 위치로
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

input_value = [35, 9, 2, 85, 17]
# print(sort_up(input_value))
# print(sort_down(input_value))
print(sel_sort(input_value))