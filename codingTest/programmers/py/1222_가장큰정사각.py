# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    #각 칸을 맨우측아래칸으로 한 가능한 가장 큰 정사각형 변의 길이를 담을 2차원 배열 bs 생성 및 초기화
    bs = []
    for i in range(len(board)):
        bs.append([0] * len(board[0]))
    #첫 줄 계산
    for y in range(len(board[0])):
        bs[0][y] = board[0][y]
    #두 번째 줄 이후 계산
    for x in range(1, len(board)):
        bs[x][0] = board[x][0]
        for y in range(1, len(board[0])):
            if board[x][y] == 0:
                bs[x][y] = 0
            else:
                bs[x][y] = min(bs[x-1][y-1], bs[x-1][y], bs[x][y-1]) + 1
    #bs 중 가장 큰 수 찾기
    side = max(map(max, bs))
    return side * side
