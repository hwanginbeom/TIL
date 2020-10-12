

def solution(info, query):
    info_list = []
    query_list = []
    for i in info:
        info_list.append(i.split(' '))
    for i in query:
        query_list.append(i.replace('and ','').split(' '))


    answer = []
    count = 0
    for i in range(0, len(query_list)):
        result_count = 0
        for j in range(0, len(info_list)):
            for z in range(0, 5):
                if z == 4:
                    if int(info_list[j][z]) >= int(query_list[i][z]):
                        count += 1
                else:
                    if query_list[i][z] == '-':
                        count += 1
                        continue
                    else:
                        if info_list[j][z] != query_list[i][z]:
                            count = 0
                            break
                        else:
                            count += 1
            else:

                if count == 5:
                    result_count += 1
                count = 0
        else:
            answer.append(result_count)

    # print(info_list)
    # print(query_list)
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)