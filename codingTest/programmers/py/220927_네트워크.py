# https://school.programmers.co.kr/learn/courses/30/lessons/43162

# 1st try
# 깊이 우선 탐색
def solution(n, computers):
    answer = 1
    tocheck = [i for i in range(1, n)]
    checking = [0]
    while len(tocheck) > 0:
        if len(checking) > 0:
            cur = checking.pop(0)
        else:
            answer += 1
            cur = tocheck.pop(0)
        for com in range(n):
            if computers[cur][com] == 1 and com in tocheck:
                tocheck.remove(com)
                checking.append(com)
    
    return answer
