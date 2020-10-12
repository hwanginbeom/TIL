# 문제 2.
# 알파벳 대소문자로 된 문자열이 주어지면,
# 이 문자열에서 가장 많이 사용된 알파벳이
# 무엇인지 출력하는 프로그램을 작성하시오.
# 단, 대소문자는 구별하지 않아요. 만약 동률이 존재하는 경우
# 알파벳 순으로 제일 앞에 있는
# 문자를 출력하세요.

# 문자열) "This is a sample Program mississippi river"
# 문자열) "abcdabcdababccddcd"

value2_1 = "This is a sample Program mississippi river"
value2_2 = "abcdabcdababccddcd"

freq = {}
for i in value2_2:
    if i in freq:
        if i == " ":
            continue
        freq[i] = freq[i] + 1
    else:
        if i == " ":
            continue
        freq[i] = 1

max_value = 0
max_alpabat = ''

for i in freq.items():
    if i[1] > max_value:
        max_alpabat = i[0]
        max_value = i[1]
    elif i[1] == max_value:
         if i[0] < max_alpabat:  # 문자열 비교 됩니다. 수정해야댐
            max_value = int(i[1])
            max_alpabat = i[0]

print("문제 2번 : {}".format(max_alpabat.upper()))


# 정답 :  "This is a sample Program mississippi river" => I
# 정답 :  "abcdabcdababccddcd" => C