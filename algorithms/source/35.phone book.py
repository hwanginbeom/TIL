# 전화번호 목록
def solution(phone_book):
    answer = True
    phone_book.sort() #내 방법대로 하기 위해서 정렬을 한 번 해줘야된다. 119가 나중에 오는경우에는 제대로 안된다.
    phone_book = list(map(str,phone_book))
    count= 0
    for i in phone_book:
        count +=1
        for j in range(count,len(phone_book)):
            if phone_book[j].find(i) == 0:
                answer = False
                return answer
    return answer