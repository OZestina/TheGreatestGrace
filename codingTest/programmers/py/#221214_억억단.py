# https://school.programmers.co.kr/learn/courses/30/lessons/138475


# 1st try => 시간 초과
def solution(e, starts):
    divisor = {}
    
    for i in range(1, e+1):
        divisor[i] = 1
        
    for i in range(2, e+1):
        for n in range(i, e + 1, i):
            divisor[n] += 1
    
    answer = []
    result = sorted(divisor, reverse=True, key=lambda x:divisor[x])
    
    for s in starts:
        for r in result:
            if r >= s:
                answer.append(r)
                break
    
    return answer
