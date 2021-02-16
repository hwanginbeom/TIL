# n = int(input())
n=4

budget_list = []
total_budget_list = []

# budget_list = [int(x) for x in input().split()]
budget_list= [110, 120, 140, 150]

# total_budget = int(input())
total_budget = 485

result = False
div_budget = (total_budget // n)

start = 0
end = max(budget_list)
result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2
    for x in budget_list:
        if x > mid:
            total += mid #떡의 양이 부족한 경우 덜 자르기
        else:
            total += x
    if total < total_budget:
        start = mid-1#떡의 양이 충분한 경우 더 자르기
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 , 여기에 result에 기록
        end = mid+1
print(result)

#
#
#
#
#
#
#
#
#
#
# while(1):
#     if result:
#         break
#     sum_budget = 0
#
#     for i in budget_list:
#         if i >= div_budget:
#             sum_budget += div_budget
#         else:
#             sum_budget += i
#     else:
#
#         total_budget_list.append(sum_budget)
#         div_budget += 1
#     if total_budget < sum_budget:
#         div_budget = div_budget - 2
#         break
#     if len(total_budget_list) > 1:
#         if total_budget_list[-1] <= total_budget_list[-2]:
#             result = True
# print(div_budget)
#
#
