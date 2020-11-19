# max_number
def solution(numbers):
    number_list = []
    for i in numbers:
        i = str(i)
        number_list.append( (i*4)[0:4] )
    number_list_index = [i[0] for i in sorted(enumerate(number_list), key=lambda x: x[1])]
    answer = ''
    for i in number_list_index[::-1]:
        answer = answer + str(numbers[i])
    answer = int(answer)
    answer = str(answer)
    return answer

numbers = 	[3, 30, 34, 5, 9]

solution(numbers)


# H-index
def solution(citations):
    citations.sort()
    max_value = 0
    for i in range(len(citations)):
        if citations[i] >= len(citations[i:]):
            max_value = len(citations[i:])
            break
    answer = max_value
    return answer

solution([ 10, 11, 12, 13])
