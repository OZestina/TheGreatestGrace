# https://school.programmers.co.kr/learn/courses/30/lessons/12927

# 1st try
# 정렬은 한 번만! (reverse = True)
# 가장 큰 수를 먼저 빼고 그 뒤의 수들과 비교하면서 차례로 진행
def solution(n, works):
    if n >= sum(works):
        return 0
    
    works.sort(reverse = True)
    t = len(works)
    while n > 0:        
        works[0] -= 1
        n -= 1
        if n == 0:
            break
            
        for i in range(1, t):
            if works[i] > works[i-1]:
                works[i] -= 1
                n -= 1
                if n == 0:
                    break
            else:
                break
                
    answer = 0
    for work in works:
        answer += work**2
    
    return answer
  
  
# 2nd try (다른 사람의 풀이)
# heap을 이용해서 푸는 방법도 있더라
# (효율성은 1st try가 조금 더 나음)

from heapq import heapify, heappush, heappop
def solution(n, works):
    heapify(works := [-i for i in works])
    for i in range(min(n, abs(sum(works)))):
        heappush(works, heappop(works)+1)
    return sum([i*i for i in works])
