"""
스러피(Slurpy) (lv.4)

스러피(Slurpy)란 어떠한 속성이 존재하는 문자열이다.
문자열을 읽어서 스러피가 존재하는지를 판단하는 프로그램을 작성해야 한다.

스럼프(Slump)는 다음 속성을 갖는 문자열이다.

첫 번째 문자가 'D' 또는 'E'이다.
첫 번째 문자 뒤에는 하나 이상의 'F'가 나온다.
하나 이상의 'F' 뒤에는 또 다른 스럼프나 'G'가 온다.
스럼프는 'F' 끝에 오는 스럼프나 'G'로끝난다.
예를 들어, DFFEFFFG는 첫 번째 문자가 'D'로 시작하고 두 개의 'F'가 나오며, 또 다른스럼프 'EFFFG'로 끝난다.
위의 경우가 아니면 스럼프가 아니다.



스림프(Slimp)는 다음 속성을 갖는 문자열이다.

첫 번째 문자는 'A'이다.
두 개의 문자로만 된 스림프면, 두 번째 문자는 'H'이다.
두 개의 문자로 된 스림프가 아니면 다음 형식 중의 하나가 된다.
'A' + 'B' + 스림프 + 'C'.
'A' + 스럼프 + 'C'.
위의 경우가 아니면 스림프가 아니다.



스러피(Slurpy)는 스림프(Slimp) 뒤에 스럼프(Slump)로 구성되는 문자열이다.

다음은 그 예이다.


Slumps : DFG, EFG, DFFFFFG, DFDFDFDFG, DFEFFFFFG
Not Slumps: DFEFF, EFAHG, DEFG, DG, EFFFFDG
Slimps: AH, ABAHC, ABABAHCC, ADFGC, ADFFFFGC, ABAEFGCC, ADFDFGC
Not Slimps: ABC, ABAH, DFGC, ABABAHC, SLIMP, ADGC
Slurpys: AHDFG, ADFGCDFFFFFG, ABAEFGCCDFEFFFFFG
Not Slurpys: AHDFGA, DFGAH, ABABCC


입력
입력될 문자열의 개수를 나타내는 정수 N 이 1 ~ 10의 범위로 우선 입력된다.
다음 줄부터 N개의 문자열이 입력된다. 문자열은 1 ~ 60 개의 알파벳 문자로 구성된다.

출력
첫 줄에는 "SLURPYS OUTPUT"을 출력한다.
N 개의 문자열 입력에 대해서 각 문자열이 스러피인지를 "YES" 또는 "NO"로 표기한다.
마지막으로 "END OF OUTPUT"를 출력한다.

Sample Input

2
AHDFG
DFGAH


Sample Output

SLURPYS OUTPUT
YES
NO
END OF OUTPUT

스림프(Slimp)는 다음 속성을 갖는 문자열이다.

첫 번째 문자는 'A'이다.
두 개의 문자로만 된 스림프면, 두 번째 문자는 'H'이다.
두 개의 문자로 된 스림프가 아니면 다음 형식 중의 하나가 된다.
'A' + 'B' + 스림프 + 'C'.
'A' + 스럼프 + 'C'.
위의 경우가 아니면 스림프가 아니다.

print(a[0:3])
Slimps: AH, ABAHC, ABABAHCC, ADFGC, ADFFFFGC, ABAEFGCC, ADFDFGC
Not Slimps: ABC, ABAH, DFGC, ABABAHC, SLIMP, ADGC

스러피(Slurpy)는 스림프(Slimp) 뒤에 스럼프(Slump)로 구성되는 문자열이다.

다음은 그 예이다.


Slumps : DFG, EFG, DFFFFFG, DFDFDFDFG, DFEFFFFFG
Not Slumps: DFEFF, EFAHG, DEFG, DG, EFFFFDG
Slimps: AH, ABAHC, ABABAHCC, ADFGC, ADFFFFGC, ABAEFGCC, ADFDFGC
Not Slimps: ABC, ABAH, DFGC, ABABAHC, SLIMP, ADGC
Slurpys: AHDFG, ADFGCDFFFFFG, ABAEFGCCDFEFFFFFG
Not Slurpys: AHDFGA, DFGAH, ABABCC

"""

def slurpy(input):
    loc = 0
    result = 'true'
    a = []
    for i in range(0, len(input)):
        if input[i] == 'C' or input[i] == 'H':
            break
        loc += 1
    slimp_value = slimp(input[0:loc+1])
    if slimp_value == 'true':
        slump_value = slump(input[loc + 1:len(input)])
        if slump_value == 'true':
            print('This is Slurpys~~~~~~~~~~!!!!!!!!!!!')
            return result
        else:
            result = 'faluse'
            print('This is not Slurpys!!!!!!!!!!!')

    else:
        result = 'faluse'
        print('This is not Slurpys!!!!!!!!!!!')

def slimp(input):
    loc = 0
    result = 'true'
    a=[]
    while(1):
        if input[loc] == 'A':
            loc += 1
            if len(input) == 2:
                input[loc] == 'H'
                print('This is slimp!!')
                break
            elif input[loc] == 'C':
                break

            elif input[loc] == 'B' :
                loc += 1
                continue
            elif input[loc] == 'H':
                if input[len(input)-1] == 'C':
                    print('This is slimp!!')
                    break
                else:
                    result = 'faluse'
                    break
            elif input[loc] == 'D' or input[loc] == 'E':
                if slump(input[loc:len(input)-1]) == 'true':
                    if input[len(input)-1] == 'C':
                        print('This is slimp!!')
                        break
                    else:
                        result = 'faluse'
                        break

        else:
            print('This is not slimp!!!!!!!!!!')
            result = 'faluse'
            break

    for i in range(0,len(input)):
        a.append(input[i])
    print(a)
    print(result)
    return result

def slump(input):
    loc = 0
    a = []
    result = 'true'
    while(1):
        if loc == len(input) - 1:
            print('This is slump!!')
            break
        if input[len(input) - 1] == 'G' and input[len(input) - 2] == 'F':
            if input[loc] == 'D' or input[loc] == 'E':
                loc += 1
                if input[loc] =='F':
                    if len(input) - 1 == loc and input[len(input)-1] == 'G':
                        print('This is slump!!')
                        break
                    for loc in range(loc,len(input)-1):
                        loc += 1
                        if input[loc] == 'F' and (input[loc+1] =='G' or input[loc+1] == 'D' or input[loc+1] == 'E' or input[loc+1] =='F'):
                            continue
                        else:
                            break
                else:
                    print('This is not slump!!!!!')
                    result = 'faluse'
                    break
        else :
            print('This is not slump!!!!!')
            result = 'faluse'
            break
    for i in range(0,len(input)):
        a.append(input[i])
    print(a)
    print(result)
    return result

    print(a)

slump('DFDFDFDFG')
print('--------------------------------------------------------')
slimp('ABAEFGCC]')
print('--------------------------------------------------------')
slurpy('ABAEFGCCDFEFFFFFG')
"""
Slimps: AH, ABAHC, ABABAHCC, ADFGC, ADFFFFGC, ABAEFGCC, ADFDFGC
Not Slimps: ABC, ABAH, DFGC, ABABAHC, SLIMP, ADGC

Slurpys: AHDFG, ADFGCDFFFFFG, ABAEFGCCDFEFFFFFG
Not Slurpys: AHDFGA, DFGAH, ABABCC
"""