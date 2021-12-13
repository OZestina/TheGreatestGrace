# https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    if n == 1: return 1
    elif n == 2: return 2
    
    a = 1
    b = 2
    for _ in range(n-2):
        a, b = b, (a+b)%1000000007
    return b
