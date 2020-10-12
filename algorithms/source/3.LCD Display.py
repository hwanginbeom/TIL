"""
3. [LCD Display]
[LCD Display]
한 친구가 방금 새 컴퓨터를 샀다. 그 친구가 지금까지 샀던 가장 강력한 컴퓨터는 공학용 전자 계산기였다. 그런데 그 친구는 새 컴퓨터의 모니터보다 공학용 계산기에 있는 LCD 디스플레이가 더 좋다며 크게 실망하고 말았다. 그 친구를 만족시킬          b      수 있도록 숫자를 LCD 디스플레이 방식으로 출력하는 프로그램을 만들어보자.

입력
입력 파일은 여러 줄로 구성되며 표시될 각각의 숫자마다 한 줄씩 입력된다. 각 줄에는 s와 n이라는 두개의 정수가 들어있으며 n은 출력될 숫자( 0<= n <= 99,999,999 ), s는 숫자를 표시하는 크기( 1<= s < 10 )를 의미한다.
0 이 두 개 입력된 줄이 있으면 입력이 종료되며 그 줄은 처리되지 않는다.

출력
입력 파일에서 지정한 숫자를 수평 방향은 '-' 기호를, 수직 방향은 '|'를 이용해서 LCD 디스플레이 형태로 출력한다.
각 숫자는 정확하게 s+2개의 열, 2s+3개의 행으로 구성된다. 마지막 숫자를 포함한 모든 숫자를 이루는 공백을 스페이스로 채워야 한다.
두 개의 숫자 사이에는 정확하게 한 열의 공백이 있어야 한다.

각 숫자 다음에는 빈 줄을 한 줄 출력한다. 밑에 있는 출력 예에 각 숫자를 출력하는 방식이 나와있다.

예
입력 예

2 12345
3 67890
0 0
출력 예

      --   --        --
   |    |    | |  | |
   |    |    | |  | |
      --   --   --   --
   | |       |    |    |
   | |       |    |    |
      --   --        --

---   ---   ---   ---   ---
|         | |   | |   | |   |
|         | |   | |   | |   |
|         | |   | |   | |   |
---         ---   ---
|   |     | |   |     | |   |
|   |     | |   |     | |   |
|   |     | |   |     | |   |
---         ---   ---   ---

"""

import numpy as np

def lcd_numbering(lcd_res, seq, point, size, lcd_num):
    lcd_list = [int(x) for x in str(lcd_num)]
    for num in lcd_list:
        if num == 1:
            lcd_res[seq][0][point] = '-' # 1
        if num == 2:
            lcd_res[seq][point][0] = 'l'  # 2
        if num == 3:
            lcd_res[seq][point][size + 1] = 'l'  # 3
        if num == 4:
            lcd_res[seq][size + 1][point] = '-' # 4
        if num == 5:
            lcd_res[seq][point + size + 1][0] = 'l'  # 5
        if num == 6:
            lcd_res[seq][point + size + 1][size + 1] = 'l'  # 6
        if num == 7:
            lcd_res[seq][size * 2 + 2][point] = '-' # 7


def lcd(size,value):
    lcd_res = []
    lcd_res2 =[]
    b = str(value)
    for i in range(0, len(b)):
        lcd_res.append([[' ' for i in range(size+2)] for j in range(2*size+3)])
        lcd_res2.append([[' ' for i in range(size+2)] for j in range(2*size+3)])
    seq = 0
    list_num = [int(x) for x in str(value)]

    for num in list_num:
        point = 1
        for j in range(0, size):
            if num == 1:
                lcd_numbering(lcd_res, seq, point, size, 36)
            if num == 2:
                lcd_numbering(lcd_res, seq, point, size, 13457)
            if num == 3:
                lcd_numbering(lcd_res, seq, point, size, 13467)
            if num == 4:
                lcd_numbering(lcd_res, seq, point, size, 2346)
            if num == 5:
                lcd_numbering(lcd_res, seq, point, size, 12467)
            if num == 6:
                lcd_numbering(lcd_res, seq, point, size, 124567)
            if num == 7:
                lcd_numbering(lcd_res, seq, point, size, 136)
            if num == 8:
                lcd_numbering(lcd_res, seq, point, size, 1234567)
            if num == 9:
                lcd_numbering(lcd_res, seq, point, size, 123467)
            if num == 0:
                lcd_numbering(lcd_res, seq, point, size, 123567)
            point = point + 1
        seq = seq + 1

    for i in range(1,seq):
        lcd_res[0] = np.hstack([lcd_res[0], lcd_res[i]])

    return lcd_res[0]


lcd_res = lcd(6, 123456)
for lcd_i in lcd_res:
    for i in lcd_i:
        print('%2s' % i, end='')
    print()
