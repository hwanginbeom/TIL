def eightCount(in_num):
    i_res = 0
    for i in range(1, in_num+1):
        cnt = str(i).count('8')
        i_res += cnt
    return i_res

print(eightCount(10000))

