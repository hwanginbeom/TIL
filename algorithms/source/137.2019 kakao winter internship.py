def solution(board, moves):
    modiv_boards=[]
    for i in range(0,len(board)):
        modiv_board=[]
        for j in range(0,len(board)):
            modiv_board.append(board[j][i])
        else:
            modiv_boards.append(modiv_board)
    basket =[]
    count = 0
    for i in range(0,len(moves)):
        for j in range(0,len(modiv_boards)):
            if modiv_boards[moves[i]-1][j] == 0 :
                continue
            else:
                number = modiv_boards[moves[i]-1][j]
                modiv_boards[moves[i]-1][j] = 0
                basket.append(number)
                if len(basket) >= 2:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        count += 1
                break
    answer = count*2
    print(answer)
    return answer

moves = [1,5,3,5,1,2,1,4]
board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
solution(board, moves)