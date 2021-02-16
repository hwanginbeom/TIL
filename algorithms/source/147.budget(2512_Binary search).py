n = int(input())
budget_list = [int(x) for x in input().split()]
total_budget = int(input())


start = 0
end = max(budget_list)

while(start <= end):
    total = 0
    mid = (start+end) // 2
    for x in budget_list:
        if x >= mid:
            total += mid #떡의 양이 부족한 경우 덜 자르기
        else:
            total += x

    if total <= total_budget:
        start = mid + 1#떡의 양이 충분한 경우 더 자르기
        result = mid
    else:
        # 최대한 덜 잘랐을 때가 정답이므로 , 여기에 result에 기록
        end = mid - 1
print(end)
