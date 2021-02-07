# 0은 자연수인가 아닌가
# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    count = 1
    
    if n == 0:
        pass
    else:
        while count < n+1:
            answer.append(x * count)
            count = count + 1
    return answer
    
# if 부분에서 pass로 하는게 맞는지 확인 필요 (0이 자연수라고 할 경우)

# range를 찾아서 새로 고침!

def solution(x,n):
    answer = []
    for i in range(n):
        answer.append(x*i + x)
    return answer

# (멋지게) 한 줄로는 이렇게 한대요

def solution(x,n):
    return [x*i + x for i in range(n)]
