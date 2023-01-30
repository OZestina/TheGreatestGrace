# https://school.programmers.co.kr/learn/courses/30/lessons/154540

# 1st try
# 처음에 재귀함수로 짰다가 너무 깊어져서 런타임에러 발생 => queue로 해결

# 다음 무인도 시작점 찾기
def get_next_island(island, h, w, x, y):
    while island[x][y] == 0:
        if y == w - 1 and x == h - 1:
            return [-1, -1]
        if y == w - 1:
            x, y = x + 1, 0
        else:
            y += 1
    return [x, y]
    

# 무인도 크기 계산
def island_food(island, h, w, x, y):
    count = 0
    q = [[x, y]]
    
    while q:
        x, y = q.pop(0)
        count += island[x][y]
        island[x][y] = 0
        
        if x + 1 < h:
            if island[x + 1][y] > 0:
                count += island[x + 1][y]
                island[x + 1][y] = 0
                q.append([x + 1, y])
        if x - 1 > -1:
            if island[x - 1][y] > 0:
                count += island[x - 1][y]
                island[x - 1][y] = 0
                q.append([x - 1, y])
        if y + 1 < w:
            if island[x][y + 1] > 0:
                count += island[x][y + 1]
                island[x][y + 1] = 0
                q.append([x, y + 1])
        if y - 1 > -1:
            if island[x][y - 1] > 0:
                count += island[x][y - 1]
                island[x][y - 1] = 0
                q.append([x, y - 1])
    return count
    
    

def solution(maps):
    h, w = len(maps), len(maps[0])
    
    # 무인도
    island = [[0] * w for _ in range(h)]
    for x in range(h):
        for y in range(w):
            if maps[x][y] != "X":
                island[x][y] = int(maps[x][y])
    
    answer = []
    x, y = get_next_island(island, h, w, 0, 0)
    while x > -1:
        answer.append(island_food(island, h, w, x, y))
        x, y = get_next_island(island, h, w, x, y)
    
    if len(answer) == 0:
        return [-1]
    return sorted(answer)
  
  
  
# 2nd try (다른 사람 풀이 참고)
# 이미 방문한 지점을 표시해 다시 연산하지 않도록 진행

# 다음 무인도 시작점 찾기
def get_next_island(maps, visited, h, w, x, y):
    while visited[x][y] == 1 or maps[x][y] == 'X':
        if y == w - 1 and x == h - 1:
            return [-1, -1]
        if y == w - 1:
            x, y = x + 1, 0
        else:
            y += 1
    return [x, y]
    

# 무인도 크기 계산
def island_food(maps, visited, h, w, x, y):
    count = 0
    q = [[x, y]]
    
    while len(q):
        x, y = q.pop(0)
        if visited[x][y] == 1:
            continue
            
        count += int(maps[x][y])
        visited[x][y] = 1
        
        if x + 1 < h:
            if visited[x + 1][y] == 0 and maps[x + 1][y] != 'X':
                q.append([x + 1, y])
        if x - 1 > -1:
            if visited[x - 1][y] == 0 and maps[x - 1][y] != 'X':
                q.append([x - 1, y])
        if y + 1 < w:
            if visited[x][y + 1] == 0 and maps[x][y + 1] != 'X':
                q.append([x, y + 1])
        if y - 1 > -1:
            if visited[x][y - 1] == 0 and maps[x][y - 1] != 'X':
                q.append([x, y - 1])
                
                
    return count
    
    

def solution(maps):
    h, w = len(maps), len(maps[0])
    
    # 무인도 방문 여부 
    island = [[0] * w for _ in range(h)]
    
    answer = []
    x, y = get_next_island(maps, island, h, w, 0, 0)
    while x > -1:
        answer.append(island_food(maps, island, h, w, x, y))
        x, y = get_next_island(maps, island, h, w, x, y)
        # print(x, y)
    
    if len(answer) == 0:
        return [-1]
    return sorted(answer)
