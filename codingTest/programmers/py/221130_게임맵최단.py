# https://school.programmers.co.kr/learn/courses/30/lessons/1844

# 1st try
def put_in_q(maps, checked, x, y, n, m, q):
    if x + 1 < n:
        if checked[x+1][y] == -1 and maps[x+1][y] != 0:
            checked[x+1][y] = checked[x][y] + 1
            q.append([x+1, y])
    if x - 1 > -1:
        if checked[x-1][y] == -1 and maps[x-1][y] != 0:
            checked[x-1][y] = checked[x][y] + 1
            q.append([x-1, y])
    if y + 1 < m:
        if checked[x][y+1] == -1 and maps[x][y+1] != 0:
            checked[x][y+1] = checked[x][y] + 1
            q.append([x, y+1])
    if y - 1 > -1:
        if checked[x][y-1] == -1 and maps[x][y-1] != 0:
            checked[x][y-1] = checked[x][y] + 1
            q.append([x, y-1])

def solution(maps):
    n, m  = len(maps), len(maps[0])
    checked = [[-1 for _ in range(m)] for _ in range(n)]
    checked[0][0] = 1
    q = [[0,0]]
    
    while len(q) > 0:
        x, y = q.pop(0)
        put_in_q(maps, checked, x, y, n, m, q)
        
    return checked[n-1][m-1]
