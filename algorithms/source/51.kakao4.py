def solution(s):
    results = []
    results2 = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2+1):
        lists = []
        for j in range(0,len(s),i):
            lists.append(s[j:j+i])
        result = ''
        count = 1
        for z in range(0, len(lists)-1):
            if lists[z] == lists[z+1]:
                count += 1
                continue
            else:
                if count == 1:
                    result = result + (lists[z])
                else:
                    result = result + (str(count) + lists[z])
                    count = 1
        else:
            if count == 1:
                results.append(len(result + lists[z+1]))
                results2.append(result + lists[z+1])

            else:
                results.append(len(result + (str(count) + lists[z])))
                results2.append(result + lists[z])


    print(results2)

    answer = min(results)
    return answer


s = "a"
print(solution(s))