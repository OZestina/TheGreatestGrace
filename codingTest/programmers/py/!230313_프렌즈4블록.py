# https://school.programmers.co.kr/learn/courses/30/lessons/17679

# 1st try
#4블록 확인
def check_4(m, n, game):
    changed = 0
    for x in range(m - 1, 0, -1):
        for y in range(n - 1, 0, -1):
            if len(game[x][y]) > 0 and len(game[x-1][y]) > 0 and len(game[x][y-1]) > 0 and len(game[x-1][y-1]) >0 and game[x][y][0] == game[x-1][y][0] == game[x][y-1][0] == game[x-1][y-1][0]:
                game[x][y] = game[x][y] + game[x][y]
                changed = 1
    return changed


#4블록 지우기
def delete_4(m, n, game):
    count = 0
    for x in range(m - 1, 0, -1):
        for y in range(n - 1, 0, -1):
            if len(game[x][y]) > 1:
                game[x][y] = ''
                count += 1
                if len(game[x-1][y]) == 1:
                    game[x-1][y] = ''
                    count += 1
                if len(game[x][y-1]) == 1:
                    game[x][y-1] = ''
                    count += 1
                if len(game[x-1][y-1]) == 1:
                    game[x-1][y-1] = ''
                    count += 1
    return count


#비어있는 블록 채우기
def down_block(m, n, game):
    for y in range(n):
        for x in range(m-1, 0, -1):
            if len(game[x][y]) == 0:
                last = x - 1
                while last > 0 and len(game[last][y]) == 0:
                    last -= 1
                game[x][y], game[last][y] = game[last][y], ''
                
                
def solution(m, n, board):
    answer = 0
    # set game board
    game = [[0] * n for _ in range(m)]
    for x in range(m):
        for y in range(n):
            game[x][y] = board[x][y]
    
    while check_4(m, n, game):
        answer += delete_4(m, n, game)
        down_block(m, n, game)
    
    return answer
