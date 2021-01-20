def solution(n, arr1, arr2):
    arr_list=[]
    for i in range(0,n):
        a=format(arr1[i], 'b').rjust(5,"0")
        b=format(arr2[i], 'b').rjust(5,"0")
        sum=''
        for j in range(0,n):
            if a[j]==1 or b[j]==1:
                sum = sum + '1'
            else:
                sum = sum +'0'
        else:
          arr_list.append(sum)
    print(arr_list)
    answer = []
    return answer

arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
n = 6
solution(n, arr1, arr2)