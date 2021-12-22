# https://programmers.co.kr/learn/courses/30/lessons/12905

# 우선 주어진 board에서 가장 크게 만들 수 있는 변(maximum)을 구하는 데까지는 완료
# maximum -> 1 의 루프에서 정사각형을 찾으면 return하는 방식으로 해보려고 하는데, 정사각형 어떻게 찾지ㅎㅎ
# 더 생각해보자!
def solution(board):
    height = len(board)
    width = len(board[0])
    total = sum([sum(x) for x in board])
    if total == 1: return 1
    
    maximum = int(max**1/2) if (int(max**1/2) < height or int(max**1/2) < width) else height if height < width
    for i in range(maximum,0,-1):
        for j in range(height-i+1):
            if [1]*i in board[j]:
                
    return 0
