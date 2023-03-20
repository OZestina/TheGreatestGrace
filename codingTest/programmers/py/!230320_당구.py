# https://school.programmers.co.kr/learn/courses/30/lessons/169198#


# 1st try
def check_short_way(m, n, startX, startY, x, y):
    length = []
    #동서남북으로 각각 쿠션하는 최단거리
    if not (startY == y and startX < x):#동
        length.append((2 * m - startX - x) ** 2 + (startY - y) ** 2)
    if not (startY == y and startX > x):#서
        length.append((startX + x) ** 2 + (startY - y) ** 2)
    if not (startX == x and startY > y):#남
        length.append((startY + y) ** 2 + (startX - x) ** 2)
    if not (startX == x and startY < y):#북
        length.append((2 * n - startY - y) ** 2 + (startX - x) ** 2)
    
    #대각선(꼭지점) 체크 => 안해도 되넹..?
    return min(length)

def solution(m, n, startX, startY, balls):
    answer = []
    
    for b in balls:
        answer.append(check_short_way(m, n, startX, startY, b[0], b[1]))    
    
    return answer
