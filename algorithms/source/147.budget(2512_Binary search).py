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
            total += mid
        else:
            total += x
    if total > total_budget:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
