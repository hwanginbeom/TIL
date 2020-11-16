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


# def solution(citations):
#     citations = sorted(citations)
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0