def solution(citations):
    citations.sort(key=lambda x: x)
    count=0
    for i in citations:
        count = count+1
        if i==len(citations)-count :
            answer=len(citations)-count+1
            break
        if i > len(citations)-count:
            answer=len(citations)-count +1
            break

    return answer

def solution2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

def solution3(citations):
    citations.sort(reverse=True)
    for i, n in enumerate(citations):
        print("##")
        print(i)
        print(n)
        if n <= i:
            return i
    return len(citations)

citations	=[3 ,0, 6, 1, 5]
citations	=[2,3,4,5,6]

print(solution(citations))

