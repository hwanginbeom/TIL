import itertools
from collections import OrderedDict


def solution(orders, course):

    # 고객의 경우의 수
    cus_list = []
    for i in orders:
        for j in course:
            if len(i) >= j:
                cus_list.append(list(map(''.join, itertools.permutations(i, j))))

    # print(cus_list)
    # print(len(cus_list))

    # 정렬
    sort_list2 = []
    value_list = []
    for i in cus_list:
        value_list=[]
        for j in i:
            value_list.append(sorted(j))
        else:
            sort_list2.append([value_list])
    # print(sort_list2[0])
    # print(sort_list2[1])


    # 중복제거
    duplicate_list2 = []
    for i in sort_list2:
        value_list1 = []
        for j in i:
            value_list2 = []
            for z in j:
                value_list2.append(''.join(z))
            else:
                value_list1.append(value_list2)
        else:
            # print(value_list1)
            duplicate_list2.append(value_list1)
    # print(duplicate_list2)
    # print(duplicate_list2[5][0])
    # print(len(duplicate_list2[0][0]))
    #


    consumer_list = []
    for i in duplicate_list2:
        for j in i:
            duplicate = set(j)
            consumer_list.append(list(duplicate))
    # print(consumer_list)
    # print(len(consumer_list))
    consumer_lists=[]
    for i in range(0,len(consumer_list)):
        consumer_lists.extend(consumer_list[i])
    # print(consumer_lists)
    # # print(consumer_lists)
    # #
    result = []
    for j in course:
        count = {}
        for i in consumer_lists:
            if len(i) == j:
                try:
                    count[i] += 1
                except:
                    count[i] = 1
        else:
            value = [k for k, v in count.items() if v == max(count.values())]
            print(value)
            if value !=[]:
                if max(count.values()) >= 2:
                    result.append(value)
    answer = []
    for i in result:
        answer.extend(i)
    answer = sorted(answer)

    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

print(solution(orders, course))