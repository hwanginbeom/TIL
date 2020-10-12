"""
알고리즘의 컨셉

각 단어에 있어서 반복을 없앤다. cookie 면 cokie 로 만든다. 그 다음에 해당하는 글자가 몇 번 반복 된지 구한다.
 cookie = 12111
 coookie = 13111

 이렇게 숫자를 구하고 각 자리수의 맞는지 비교하고 ( 5 / 5 )

 그다음 각 자리수 단어가 맞는지 비교한다. c = c  / o = o  / k = k / i =  i / e = e
"""


def getCharCount(word):
    c_list = []
    n_list = []
    for i in word:
        if len(c_list) == 0:
            c_list.append(i)
            n_list.append(1)
        if len(c_list) > 0:
            if i != c_list[-1]:
                c_list.append(i)
                n_list.append(1)
            else:
                n_list[-1] += 1
    return c_list, n_list


def wordComp(src_word, tgt_word):
    s_clist, s_nlist = getCharCount(src_word)
    t_clist, t_nlist = getCharCount(tgt_word)
    b_res = False
    if s_clist == t_clist:
        for i in range(len(s_nlist)):
            if s_nlist[i] > t_nlist[i]:
                break
        else:
            b_res = True
    return b_res


print(wordComp('cookie', 'coookie'))