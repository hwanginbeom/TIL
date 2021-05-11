n=8
k=2
cmd =["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

answer=''
for i in range(8):
    answer += 'O'
number = k
delete_number = 0
answer2 = answer.copy()
for i in range(0, len(cmd)):
    a, b = cmd[i].split(' ')
    if a == 'U':
        number += b
    elif a == 'D':
        number += b
    elif a == 'C':
        del answer2[1]
        answer[k] = 'X'
        delete_number = k
    elif a == 'Z':
        if delete_number < k:
            k+=1
            answer[delete_number] = 'O'
        else:
            answer[delete_number] = 'O'

print(cmd[0])
a,b=cmd[0].split(' ')
print(a)
print(b)
print(cmd[0].split(' '))
