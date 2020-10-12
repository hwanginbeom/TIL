import string

def solution(new_id):
    answer = ''

    # 1 단계
    def step1(new_id):
        answer = new_id.lower()
        return answer

    # 2 단계
    def step2(answer):
        for i in answer:
            if i not in string.ascii_lowercase+"-_.0123456789":
                answer = answer.replace(i, '')
        return answer



    # 3단계
    def step3(answer):
        while(1):
            if answer.find('..') != -1:
                answer = answer[0:answer.find('..')]+answer[answer.find('..')+1:]
            else:
                break
        return answer


    # 4단계
    def step4(answer):
        while(1):
            if answer[0] != '.':
                if answer[-1] != '.':
                    break
                else:
                    answer = answer[:len(answer)-1]
            else:
                if len(answer) == 1:
                    answer = ''
                    break
                else:
                    answer = answer[1:]
        return answer


    # 5 단계
    def step5(answer):
        if answer == '':
            answer = 'a'
        return answer


    # 6단계
    def step6(answer):
        if len(answer) > 15:
            answer = answer[:15]
        return answer


    # 7단계
    def step7(answer):
        while(1):
            if len(answer) < 3:
                answer = answer+answer[-1]
            else:
                break
        return answer

    answer = step1(new_id)
    answer = step2(answer)
    answer = step3(answer)
    answer = step4(answer)
    answer = step5(answer)
    answer = step6(answer)
    answer = step4(answer)
    answer = step7(answer)

    return answer

print(solution("=.="))