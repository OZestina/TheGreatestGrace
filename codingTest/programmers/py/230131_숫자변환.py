# https://school.programmers.co.kr/learn/courses/30/lessons/154538#

# 1st try
# 초반에 2의 제곱, 3의 제곱만 생각하다가 실패
# 재귀로하면 too deep해져서 런타임 에러 발생 => dfs, queue로 해결
def counter(x, y, n, i, number, stack):
    if x == y / 2 or x == y / 3 or x == y - n:
        return i + 1
    
    if y % 2 == 0 and x < y // 2:
        stack.append([y // 2, i + 1])
    if y % 3 == 0 and x < y // 3:
        stack.append([y // 3, i + 1])
    if y - n > x:
        stack.append([y - n, i + 1])
    return -1

def solution(x, y, n):
    
    if x == y: return 0
    
    stack = [[y, 0]]
    while len(stack):
        y, i = stack.pop(0)
        answer = counter(x, y, n, i, number, stack)
        if answer > -1: return answer
    
    return -1
  
  
# 2nd try
# 6배수 등을 visited로 재연산하지 않도록 진행. 훨씬 빨라졌다
def counter(x, y, n, i, visited, stack):
    if x == y / 2 or x == y / 3 or x == y - n:
        return i + 1
    
    if y % 2 == 0 and x < y // 2 and visited[y // 2] == 0:
        stack.append([y // 2, i + 1])
        visited[y // 2] = 1
    if y % 3 == 0 and x < y // 3 and visited[y // 3] == 0:
        stack.append([y // 3, i + 1])
        visited[y // 3] = 1
    if y - n > x and visited[y - n] == 0:
        stack.append([y - n, i + 1])
        visited[y - n] = 1
    return -1

def solution(x, y, n):
    
    if x == y: return 0
    
    visited = [0] * (y + 1)
    stack = [[y, 0]]
    while len(stack):
        y, i = stack.pop(0)
        answer = counter(x, y, n, i, visited, stack)
        if answer > -1: return answer
    
    return -1
