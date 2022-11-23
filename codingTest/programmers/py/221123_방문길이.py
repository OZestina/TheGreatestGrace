# https://school.programmers.co.kr/learn/courses/30/lessons/49994

# 1st try
# 지나간 길을 이중배열로 저장, 각 점마다 U, L만 기록해서 계산 편하게 함
def cango(cur, d): #갈 수 있는 길인지 확인
    if d == 'U':
        if cur[1] - 1 < 0: return 0
    elif d == 'D':
        if cur[1] + 1 > 10: return 0
    elif d == 'R':
        if cur[0] + 1 > 10: return 0
    else:# d == 'L'
        if cur[0] - 1 < 0: return 0
    return 1


def newroad(arr, cur, d): #이미 지나간 길인지 확인 (UL = 11)
    if d == 'U':
        if arr[cur[0]][cur[1]] > 9: return 0
        arr[cur[0]][cur[1]] += 10
    else: # d == 'L'
        if arr[cur[0]][cur[1]] % 10 > 0: return 0
        arr[cur[0]][cur[1]] += 1
    return 1
    

def solution(dirs):
    answer = 0
    arr = [[0 for i in range(11)] for j in range(11)] #지나간 길 저장용

    cur = [5,5]
    for d in dirs:
        if cango(cur, d) == 0: continue
        
        if d == 'U':
            answer += newroad(arr, cur, d)
            cur[1] -= 1
        elif d == 'D':
            cur[1] += 1
            answer += newroad(arr, cur, 'U')
        elif d == 'R':
            cur[0] += 1
            answer += newroad(arr, cur, 'L')
        else: #d == 'L'
            answer += newroad(arr, cur, d)
            cur[0] -= 1
    
    return answer
  
  
  
# 2nd try (다른 사람의 풀이)
# 훨씬 짧고, 두 배 정도 빠르다(!!)
# 지나간 길을 양 방향에서 set()에 저장하는 방식으로 진행 (set여서 빠른건가)
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
