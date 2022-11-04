# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 전역변수를 활용하면 쉽게 해결되는 부분이 있었는데, 없이 풀려다가 (사실 생각도 못했음ㅎ) 시간 오래걸렸다
# 한 줄로 푸는 방법도 있던데 이해 못함 (4th try)


# 1st try
# set() 활용해서 max()값 리턴
def enter_dungeons(k, dungeons, arr):
    count = 0
    for i in arr:
        if k >= dungeons[i][0]:
            k -= dungeons[i][1]
            count += 1
    return count


def rec_exhaustive(k, dungeons, n, idx, arr, dun):
    if idx == n:
        dun.add(enter_dungeons(k, dungeons, arr))
        return
    temp = arr[:]
    for i in range(n):
        if i not in temp:
            temp[idx] = i
            rec_exhaustive(k, dungeons, n, idx+1, temp, dun)

            
def solution(k, dungeons):
    arr = [-1 for i in range(len(dungeons))]
    dun = set()
    rec_exhaustive(k, dungeons, len(dungeons), 0, arr, dun)
    
    return max(dun)
    

    
# 2nd try
def enter_dungeons(k, dungeons, arr):
    count = 0
    for i in arr:
        if k >= dungeons[i][0]:
            k -= dungeons[i][1]
            count += 1
    return count


def rec_exhaustive(k, dungeons, n, idx, arr, answer):
    if idx == n:
        count = enter_dungeons(k, dungeons, arr)
        answer = count if answer < count else answer
        return answer
    
    temp = arr[:]
    for i in range(n):
        if i not in temp:
            temp[idx] = i
            answer = rec_exhaustive(k, dungeons, n, idx+1, temp, answer)
    return answer
            
def solution(k, dungeons):
    arr = [-1 for i in range(len(dungeons))]
    return rec_exhaustive(k, dungeons, len(dungeons), 0, arr, 0)
  
  
  
  
# 3rd try (다른 사람의 풀이)
# 전역변수와 visited[i]를 사용해서 for문을 한 번만 사용
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        print(j, k, visited)
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
  
  
# 4th try (다른 사람의 풀이)
# 리턴값이 어디있는거지...?
solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])
