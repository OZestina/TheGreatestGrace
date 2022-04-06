# https://programmers.co.kr/learn/courses/30/lessons/12978#

# 1st try => 50% 성공
def solution(N, road, K):
    time = [-1] + [0] + [-1] * (N-1)
    q = [1]
    checked = []
    while len(q) > 0:
        town = q.pop(0)
        checked.append(town)
        for i in road:
            if i[0] == town:
                if i[1] not in checked:
                    q.append(i[1])
                    if time[i[1]] == -1:
                        time[i[1]] = time[i[0]] + i[2]
                    else:
                        time[i[1]] = time[i[0]] + i[2] if time[i[0]] + i[2] < time[i[1]] else time[i[1]]
            elif i[1] == town:
                if i[0] not in checked:
                    q.append(i[0])
                    if time[i[0]] == -1:
                        time[i[0]] = time[i[1]] + i[2]
                    else:
                        time[i[0]] = time[i[1]] + i[2] if time[i[1]] + i[2] < time[i[0]] else time[i[0]]
    
    answer = 0
    for i in time:
        if i <= K: answer += 1
    
    return answer-1
  
  
# 2nd try => 성공
# 1st try는 돌아가는 길이 더 짧을 수 있는 가능성을 배제한 코드였다
def solution(N, road, K):
    time = [-1] + [0] + [None] * (N-1)
    q = [1]
    
    while len(q) > 0:
        town = q.pop(0)
        for i in road:
            if i[0] == town or i[1] == town:
                if i[0] == town: new = i[1]
                elif i[1] == town: new = i[0]
                
                if time[new] == None:
                    q.append(new)
                    time[new] = time[town] + i[2]
                elif time[town] + i[2] < time[new]:
                    q.append(new)
                    time[new] = time[town] + i[2] if time[town] + i[2] < time[new] else time[new]
    
    return len([town for town in time if town <= K]) - 1
  
  
# 3rd try : 다른 사람의 풀이 참고
# 마을을 한 번씩만 방문하면서 계산하는 방법. 
def solution(N, road, K):
    visited = [False]*(N+1) #마을 방문여부
    D = [500001]*(N+1)      #태초마을에서의 거리 (초기 최솟값은 "K의최댓값+1"로 설정)
    r = [[(None, None)]] + [[] for _ in range(N)]   #각 마을에서 연결된 마을까지의 루트 저장용
    
    #각 마을에서 연결된 마을까지의 루트 계산 및 저장
    for route in road:
        r[route[0]].append((route[1], route[2]))
        r[route[1]].append((route[0], route[2]))
    
    #태초마을 거리 0으로 세팅
    D[1] = 0
    
    #거리 계산
    for _ in range(1,N+1): 
        min_ = 500001
        #방문하지 않은 마을 중 가장 가까운 마을부터 방문
        for i in range(1,N+1): 
            if not visited[i] and D[i] < min_:
                min_ = D[i]
                current = i
        visited[current] = True
        
        for toWhere, howFar in r[current]:
            temp = D[current] + howFar
            D[toWhere] = temp if temp < D[toWhere] else D[toWhere]

    #조건에 맞는 마을 세기
    return len([d for d in D if d <= K])
