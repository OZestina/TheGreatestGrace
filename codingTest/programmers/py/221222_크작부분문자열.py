# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def smaller_than_p(t, start, p):
    for i in range(len(p)):
        if p[i] > t[start + i]:
            return 1
        elif p[i] < t[start + i]:
            return 0
    else:
        return 1

def solution(t, p):
    answer = 0
    
    for i in range(len(t) - len(p) + 1):
        answer += smaller_than_p(t, i, p)
                
    return answer
