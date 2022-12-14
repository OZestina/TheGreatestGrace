# https://school.programmers.co.kr/learn/courses/30/lessons/68645

# 1st try
# n x n 대신 삼각형 배열로 만들면 시간 단축 & 리스트 합칠 때 편함 (line 27)
# sum(list(), []) 이 방법은 너무 느리니 쓰지 말자... (line 42)
def go_down(pyramid, x, y, num, n):
    while x + 1 < n and pyramid[x+1][y] == 0:
        num += 1
        pyramid[x+1][y] = num
        x += 1
    return [x, y, num]
    
def go_right(pyramid, x, y, num, n):
    while y + 1 < n and pyramid[x][y+1] == 0:
        num += 1
        pyramid[x][y+1] = num
        y += 1
    return [x, y, num]
    
def go_up(pyramid, x, y, num, n):
    while pyramid[x-1][y-1] == 0:
        num += 1
        pyramid[x-1][y-1] = num
        x, y = x-1, y-1
    return [x, y, num]

def solution(n):
    pyramid = [[0] * i for i in range(1, n+1)]
    # 기존 방법: pyramid = [[0 for _ in range(n)] for _ in range(n)]
    
    pyramid[0][0] = 1
    x, y, num = 0, 0, 1
    
    for _ in range((n - 1) // 3 + 1):
        x, y, num = go_down(pyramid, x, y, num, n)
        x, y, num = go_right(pyramid, x, y, num, n)
        x, y, num = go_up(pyramid, x, y, num, n)
    
    answer = []
    for i in range(n):
        answer += pyramid[i]
    # answer = sum(pyramid, [])
    
    return answer
