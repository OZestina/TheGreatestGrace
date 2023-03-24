# https://school.programmers.co.kr/learn/courses/30/lessons/172928

# 1st try
def check_start(park):
    for i in range(len(park)):
        if "S" in park[i]:
            for j in range(len(park[0])):
                if park[i][j] == "S":
                    return [i, j]
    
    
def check_route(route, park, pos):
    x, y = pos
    direc = route[0]
    step = int(route[2])
    
    if direc == "E":
        if len(park[0]) <= y + step:
            return
        for s in range(1, step + 1):
            if park[x][y + s] == "X":
                return
        pos[1] += s
    elif direc == "W":
        if y - step < 0:
            return
        for s in range(1, step + 1):
            if park[x][y - s] == "X":
                return
        pos[1] -= s
    elif direc == "N":
        if x - step < 0:
            return
        for s in range(1, step + 1):
            if park[x - s][y] == "X":
                return
        pos[0] -= s
    else: # "S"
        if len(park) <= x + step:
            return
        for s in range(1, step + 1):
            if park[x + s][y] == "X":
                return
        pos[0] += s
        
        
def solution(park, routes):
    # 시작 위치 확인
    pos = check_start(park)
    # 각 명령마다 실행 가능한지 체크하며 위치 변경
    for route in routes:
        check_route(route, park, pos)
    
    return pos
