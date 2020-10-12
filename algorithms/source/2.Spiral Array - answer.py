def spiral(nx, ny):
    s = [[-1 for i in range(ny)] for j in range(nx)]

    x, y = 0, 0
    dx, dy = 0, 1
    num = 0
    while s[x][y] == -1:
        s[x][y] = num
        x, y = x+dx, y+dy
        num += 1

        if y >= ny or x >= nx or s[x][y] != -1:
            x, y = x-dx, y-dy
            dx, dy = dy, -dx
            x, y = x+dx, y+dy
    return s


arr_res = spiral(5, 6)
print(arr_res)
for arr_i in arr_res:
    for i in arr_i:
        print('%2s' % i, end='')
    print()