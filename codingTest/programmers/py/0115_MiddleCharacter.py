#https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3

def solution(s):
    long = len(s)
    if long % 2 ==1:
        answer = s[long//2]
    else:
        answer = s[long//2-1:long//2+1]
    
    return answer
    
# 쉬웠음
# 하나 더풀어야징
