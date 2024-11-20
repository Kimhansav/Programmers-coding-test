def solution(board, moves):
    answer = 0
    basket = []
    new_list = [[board[-i-1][j] for i in range(len(board)) if board[-i-1][j] != 0] for j in range(len(board[0]))] 
    print('new_list: ', new_list)
    for move in moves:
        move -= 1
        if len(new_list[move]) > 0:
            basket.append(new_list[move].pop())
            print(f'{move} basket: ', basket)
            if len(basket) > 1 and basket[-1] == basket[-2]:
                basket = basket[:-2]
                answer += 2
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))