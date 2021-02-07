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
