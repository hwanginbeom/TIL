def solution(board, moves):
    lists = []
    for i in range(0,len(board)):
        list = []
        for j in range(0,len(board)):
            if board[len(board)-1 -j][len(board)-1-i] == 0:
                continue
            list.append(board[len(board)-1 -j][len(board)-1-i])
        else:
            lists.append(list)
    print(lists)
    basket = []
    for i in moves:
        basket.append(lists[i-1].pop())
    count = 0
    print(basket)
    # while(1):
    #     if len(basket) >= 2:
    #         basket


    lists[0].pop()
    print(lists)
    answer = 0
    return answer

board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)