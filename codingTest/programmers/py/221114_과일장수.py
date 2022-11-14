# https://school.programmers.co.kr/learn/courses/30/lessons/135808 

# 1st try
def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    for i in range(len(score) // m):
        answer += score[(i + 1) * m - 1] * m
    
    return answer
  
  
  
# 2nd try
# 정렬을 안하는 방법, 조금 더 빠르다
def solution(k, m, score):
    lst = [0 for i in range(k + 1)]
    for i in score: lst[i] += 1
    
    answer = 0
    temp = 0
    for i in range(k, 0, -1):
        temp += lst[i]
        answer += temp // m * i * m
        temp -= temp // m * m
    
    return answer
