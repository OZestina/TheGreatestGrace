# https://school.programmers.co.kr/learn/courses/30/lessons/160585

# 1st try
# 완전 하드코딩했다. 그래도(그래서?) 시간은 빠르다
# 정상 게임의 경우의 수를 모두 생각해야해서 곤란했던 문제

def solution(board):
    
    # count = [O 개수, X 개수, O 빙고 수, X 빙고 수]
    count = [0, 0, 0, 0]
    for i in range(3):
        for j in range(3):
            if i == j == 0: #대각선1 빙고 count
                if board[0][0] == board[1][1] == board[2][2] == "O":
                    count[2] += 1
                elif board[0][0] == board[1][1] == board[2][2] == "X":
                    count[3] += 1
            elif i == 0 and j == 2:   #대각선2 빙고 count
                if board[0][2] == board[1][1] == board[2][0] == "O":
                    count[2] += 1
                elif board[0][2] == board[1][1] == board[2][0] == "X":
                    count[3] += 1
            if i == 0:  #세로 빙고 수 count
                if board[0][j] == board[1][j] == board[2][j] == "O":
                    count[2] += 1
                elif board[0][j] == board[1][j] == board[2][j] == "X":
                    count[3] += 1
            if j == 0:  #가로 빙고 수 count
                if board[i][0] == board[i][1] == board[i][2] == "O":
                    count[2] += 1
                elif board[i][0] == board[i][1] == board[i][2] == "X":
                    count[3] += 1
            # O, X 개수 count
            if board[i][j] == "O":
                count[0] += 1
            elif board[i][j] == "X":
                count[1] += 1
                
    if count[2] == 2 and count[0] - count[1] == 1:
        return 1
    if 1 < count[0] - count[1] or count[0] - count[1] < 0:
        return 0
    if count[2] + count[3] > 1:
        return 0
    if count[2] and count[0] == count[1]:
        return 0
    if count[3] and count[0] > count[1]:
        return 0
    
    
    return 1
