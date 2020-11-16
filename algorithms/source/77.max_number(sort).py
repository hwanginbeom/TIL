# def solution(numbers) :
#     numbers = list(map(str, numbers))
#     numbers.sort(key = lambda x : x*3, reverse = True)
#     answer = ''.join(numbers)
#     return answer

def solution(numbers):
    number_list = []
    for i in numbers:
        i = str(i)
        number_list.append( (i*4)[0:4] )
    print(number_list)
    number_list_index = [i[0] for i in sorted(enumerate(number_list), key=lambda x: x[1])]
    print(number_list_index)
    answer = ''
    for i in number_list_index[::-1]:
        answer = answer + str(numbers[i])
    print(answer)
    answer = int(answer)
    answer = str(answer)
    return answer

numbers = 	[3, 30, 34, 5, 9]




solution(numbers)