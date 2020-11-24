# 1717 - Representation of a set(집합의 표현)

# 특정 원소가 속한 집합을 찾기
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
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화 하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    c, a, b = map(int, input().split())
    if c == 0:
        # union 연산을 각각 수행
        union_parent(parent, a, b)

    if c == 1:
        # 각 원소가 속한 집합 출력하기
        # print('각 원소가 속한 집합:', end='')
        # for i in range(1, v + 1):
        value_1 = find_parent(parent, a)
        value_2 = find_parent(parent, b)
        if value_1 == value_2:
            print('YES')
        else:
            print('NO')
        # print(value_1)
        # print(value_2)
        # print()



# # 부모 테이블 내용 출력하기
# print('부모 테이블: ', end='')
# for i in range(1, v + 1):
#     print(parent[i], end='')


if __name__ == "__main__":
    n = int(input())  # 총 도시의 수
    m = int(input())  # 여행 계획에 속한 도시들의 수
    graph = [list(map(int, input().split())) for _ in range(n)]
    move = list(map(int, input().split()))

    # 플로이드-워셜 알고리즘을 통해 모든 노드 간의 최소 거리를 구한다.
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and i != j:  # 길이 없다는 뜻
                graph[i][j] = 1e9  # 10억으로 대입

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 여행 여부 확인
    flag = True
    pre_index = move[0] - 1
    for i in range(1, m):
        if graph[pre_index][move[i] - 1] >= 1e9:  # 길이 없는 경우
            flag = False
            break
        else:
            pre_index = move[i] - 1

    if flag:
        print("YES")
    else:
        print("NO")