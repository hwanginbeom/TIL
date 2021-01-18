stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5
def solution(N, stages):
    result = {} # 딕셔너리로 설정
    denominator = len(stages) # 길이
    for i in range(1, N+1): # 본문에 나와있는 그대로 실행
        if denominator != 0: # 만약 길이가 0이 아니면
            count = stages.count(i) # 받은 stages를 count로 갯수를 세는데 있어서 1부터 시작한다. 이것의 개수를 센다
            result[i] = count / denominator # 전체 길이에서 해당 개수를 나눈 값을 딕셔너리의 value으로 해서 넣는다.
            denominator -= count #해당 갯수만큼 전체의 길이를 줄여준다
        else:
            result[i] = 0
    print(result)
    return sorted(result, key=lambda x : result[x], reverse=True) # sorted를 하는데 람다를 이용해서 key에 있는 value에 대한 정렬을 한다. 그냥 result를 넣으면 key에 대한 sorted 가 된다.