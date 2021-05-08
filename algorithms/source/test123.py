# test30분
s = 'one4seveneight'

eng_list = ['zero','one','two','three','four','five','six','seven','eight','nine']
number_list=['0','1','2','3','4','5','6','7','8','9']
true_number = ''
for i in range(0,len(s)):
    true_false = 'false'
    for j in number_list:
        if s[i] == j:
            true_number += s[i]
            true_false = 'true'
            break
        else:
            true_false = 'false'
    if true_false=='false':
        for z in range(0,len(eng_list)):
            if s[i:i+len(eng_list[z])] == eng_list[z]:
                true_number += str(z)
print(true_number)