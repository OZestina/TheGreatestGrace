# https://programmers.co.kr/learn/courses/30/lessons/81302

# 22.12.29
# 1st try => 성공
# 사람 사이의 거리를 계산해서 푸는 (그 생각만 했다면) 간단한 문제였다
#                       => 1이면 사람끼리 붙어있는거니까 실패
#                       => 2면 그 사이/대각선의 지형지물을 고려해서 성공/실패 리턴 (check_ok 함수)
def check_ok(place, h, t):
    if h[0] == t[0]:
        if place[h[0]][(h[1]+t[1])//2] == "O":
            return 0
    elif h[1] == t[1]:
        if place[(h[0]+t[0])//2][h[1]] == "O":
            return 0
    else:
        if place[h[0]][t[1]] == "O" or place[t[0]][h[1]] == "O":
            return 0
    return 1

def solution(places):
    answer = []
    
    for i in range(len(places)):
        #사람의 위치 확인
        human = []
        for x in range(5):
            for y in range(5):
                if places[i][x][y] == "P":
                    human.append([x, y])
        #human에 있는 사람들 위치를 1:1로 비교 및 확인
        for h in range(len(human)-1):
            for t in range(h+1, len(human)):
                temp = abs(human[h][0]-human[t][0]) + abs(human[h][1]-human[t][1])
                if temp == 1:
                    answer.append(0)
                    break
                elif temp == 2:
                    if check_ok(places[i], human[h], human[t]) == 0:
                        answer.append(0)
                        break
            if len(answer) > i:
                break
        else:
            answer.append(1)
            
    return answer
