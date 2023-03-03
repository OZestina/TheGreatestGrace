# https://school.programmers.co.kr/learn/courses/30/lessons/161990

# 1st try
# 모두 탐색
def solution(wallpaper):
    answer = [51, 51, 0, 0]
    
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == "#":
                if x < answer[0]:
                    answer[0] = x
                if y < answer[1]:
                    answer[1] = y
                if answer[2] < x + 1:
                    answer[2] = x + 1
                if answer[3] < y + 1:
                    answer[3] = y + 1
    return answer
  
  
# 2nd try
# 상하좌우에서 가장 가까운 애들만 체크
def solution(wallpaper):
    answer = [-1, -1, -1, -1]
    len_x = len(wallpaper)
    len_y = len(wallpaper[0])
    
    for x in range(len_x):
        if "#" in wallpaper[x]:
            answer[0] = x
            break
    for x in range(len_x - 1, -1, -1):
        if "#" in wallpaper[x]:
            answer[2] = x + 1
            break
    for y in range(len_y):
        for x in range(len_x):
            if "#" in wallpaper[x][y]:
                answer[1] = y
                break
        if answer[1] > -1:
            break
    for y in range(len_y - 1, -1, -1):
        for x in range(len_x):
            if "#" in wallpaper[x][y]:
                answer[3] = y + 1
                break
        if answer[3] > -1:
            break
            
    return answer
