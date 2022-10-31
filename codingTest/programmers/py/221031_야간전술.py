# https://school.programmers.co.kr/learn/courses/30/lessons/133501 

# 1st try
def solution(distance, scope, times):
    answer = distance
    
    for i in range(len(scope)):
        div = sum(times[i])
        
        ran1, ran2 = sorted(scope[i])
        
        for r in range(ran2 - ran1 + 1):
            if (ran1 + r - 1) % div + 1 <= times[i][0]:
                killed = ran1 + r
                answer = killed if killed < answer else answer
                break
        
    return answer
  
  
# 2nd try (다른 사람의 풀이 참고)
# enumerate 와 min의 사용..! 기억해두자
def solution(distance, scope, times):
    answer = distance

    for i,s in enumerate(scope):
        s.sort()
        for t in range(s[0], s[1]+1):
            if (t - 1) % sum(times[i]) + 1 <= times[i][0]:
                answer = min(answer, t)
                break

    return answer
