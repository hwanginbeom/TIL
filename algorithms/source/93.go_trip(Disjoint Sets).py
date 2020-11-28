# 1976 - Let's go on a trip

def find_parent(parent, x):
    # 루트 노드를 찾을 떄까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
# v, e = map(int, input().split())
v = int(input())

parent = [0] * (v + 1)  # 부모 테이블 초기화 하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

e = int(input())
a,b,c = map(int, input().split())
# print(list_array)
for i in range(v):
    list_array = []
    list_array.append(map(int, input().split()))
    print(list_array)
#     a, b, c =
#     if a == 1:
#         print()
#     elif b==
