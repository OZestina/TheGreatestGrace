# https://school.programmers.co.kr/learn/courses/30/lessons/142085#

# 1st try
# 정렬이 필요할 때는 heapq를 사용하자..!
from heapq import heappop, heappush

def solution(n, k, enemy):
    #무적권 짱짱
    if k >= len(enemy):
        return len(enemy)
    
    answer = k
    passed = []
    for i in range(k):
        heappush(passed, enemy[i])
        
    for i in range(k, len(enemy)):
        min_pass = passed[0]
        if enemy[i] > min_pass:
            if min_pass <= n:
                n -= min_pass
                answer += 1
            else:
                return answer
            heappop(passed)
            heappush(passed,enemy[i])
            
        else:
            if enemy[i] <= n:
                n -= enemy[i]
                answer += 1
            else:
                return answer
        
        
    return answer
