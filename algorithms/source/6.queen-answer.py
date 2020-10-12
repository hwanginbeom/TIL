"""
[Eight Queens Problem]

8-queens 문제는 Queen이 다른 Queen를 공격할 수 없는 8 X 8개의 체스 판에서 8개의 Queen을 체스판 위에 놓이게하는 문제이다.
체스 판에서 Queen은 똑같은 행렬(가로와 세로)/대각선방향에 대해서 공격이 가능하다.
그러므로 이 문제에 대한 solution은 자기 자신(Queen)을 보호하면서 새로운 위치에 Queen을 놓게 하는 것이다.

1. 각 열에는 오직 하나의 퀸만 존재해야 한다.
2. 각 행에는 오직 하나의 퀸만 존재해야 한다.
3. 각각의 퀸의 대각선에 다른 퀸이 존재해서는 안 된다.

예를들어 다음과 같이 퀸을 위치할 수 있다.




8 x 8 체스판에 8개의 Queen을 놓을 수 있는 방법은 모두 몇 가지인가?

이 문제에서 배울 점

1.재귀함수
2. 배열 + 배열
 ex )  [1,2,3] + [3,2,1] = [1,2,3,3,2,1]
3. for else 문  -> for문에 break 없이 다 돌 경우에 else 에 있는게 실행된다.
"""

N = 8


def placeQueen(queen_pos):
    res = 0
    n = len(queen_pos)
    if n == N:
        return 1
    for i in range(N): #i는 n번 반복
        for j in range(n): # j도 n번 반복
            if i == queen_pos[j]: #배열 [j] 의 값과 i 가 같으면 첫번째 행에서 걸리기 때문에 멈춘다.
                break
            if n - j == i - queen_pos[j]:
                break
            if n - j == queen_pos[j] - i:
                break
        else:
            res += placeQueen(queen_pos + [i]) # 재귀 함수 + 배열을 배열로 더 할 수 있다.
    return res


print(placeQueen([]))
