# https://school.programmers.co.kr/learn/courses/30/lessons/12952

# 1st try => 아슬아슬하게 통과 (시간초과)
def check_pos(chess, n, x, y):
    #check for up
    for i in range(0, x):
        if chess[i][y] == 1: return 0
    #check for left_diagonal
    for i in range(1, y + 1):
        if chess[x - i][y - i] == 1: return 0
    #check for right_diagonal
    for i in range(1, n - y):
        if chess[x - i][y + i] == 1: return 0
    return 1

def fill_queen(chess, n, time):
    if time == n:
        return 1
    
    count = 0
    for i in range(n):
        if check_pos(chess, n, time, i):
            chess[time][i] = 1
            count += fill_queen(chess, n, time + 1)
            chess[time][i] = 0
    return count

def solution(n):
    answer = 0
    chess = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        chess[0][i] = 1
        answer += fill_queen(chess, n, 1)
        chess[0][i] = 0
    
    return answer
  
  
# 2nd try (다른 사람의 풀이 참고)
#왼대각선, 오른대각선, 수직을 제외하는 것을 x, y 좌표의 차로 한 번에 해결. 멋져..!
#왼대각석, 오른대각선의 경우 MAX_N * 2 - 1 개이나, 1을 빼주지 않아도 문제없고 빼지 않는것이 연산이 줄어들어 더 낫다. (메모리상으로도 미미한 차이일듯)

# n <= 12 제한조건
MAX_N = 12

def put_queen(n, check_y, check_l_dia, check_r_dia, x):
    # 맵이 모두 채워졌을 경우
    if x == n: return 1

    count = 0
    for q in range(n):
        if check_y[q] or check_l_dia[x + q] or check_r_dia[q - x]:
            continue
        check_y[q] = check_l_dia[x + q] = check_r_dia[q - x] = True
        count += put_queen(n, check_y, check_l_dia, check_r_dia, x + 1)
        check_y[q] = check_l_dia[x + q] = check_r_dia[q - x] = False
    return count

def solution(n):
    check_y = [False for _ in range(MAX_N)]
    check_l_dia = [False for _ in range(MAX_N * 2)] # 왼대각선: x + y 값
    # 오른대각선: y - x 값 => 범위는 -(n-1) ~ n-1
    # 별도 처리를 해주지 않아도 음수인덱스로 접근 가능해 문제없다
    check_r_dia = [False for _ in range(MAX_N * 2)]
    
    answer = put_queen(n, check_y, check_l_dia, check_r_dia, 0)
    
    return answer
