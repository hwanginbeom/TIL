s = "ababcdcdababcdcd"


def solution(s):
    list_numbers = []
    answer=[]
    if len(s)==1:
        answer = len(s)
        return answer
    for i in range(1, round(len(s) / 2)+1):
        list_number = []
        count = 1
        for j in range(0, len(s), i):
            if s[j:j + i] == s[j + i:j + i + i]:
                if len(s[j + i:j + i + i]) == i:
                    count += 1
                else:
                    list_number.append(s[j:j + i])
                    list_number.append(s[j:j + i + i])
                    break
            else:
                if count == 1:
                    list_number.append(s[j:j + i])
                else:
                    list_number.append(str(count) + s[j:j + i])
                    count = 1
        else:
            if count != 1:
                list_number.append(str(count) + s[j:j + i])
            if (len(s) - j)%i != 0:
                list_number.append(s[j + i:j + i + i])
            list_numbers.append(list_number)
    print(list_numbers)
    for i in range(0,len(list_numbers)):
        answer.append(len(''.join(list_numbers[i])))

    print(answer)
    answer = min(answer)
    return answer


solution(s)


def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))
