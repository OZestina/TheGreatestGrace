# https://programmers.co.kr/learn/courses/30/lessons/62048#


# 1st try => 실패(16, 18번 시간초과)
# 최대공약수로 계산 범위를 줄이고, 기울기로 좌표를 구해서 못쓰는 사각형을 구하는 방법
import math

def solution(w,h):
    gcd = math.gcd(w,h)
    
    answer = 0 
    nw = int(w/gcd)
    nh = int(h/gcd)
    
    temp = 0
    for i in range(1, nh+1):
        answer += int( (i * nw -1) / nh + 1) - temp
        temp = int(i/nh * nw)
    
    return w*h - answer * gcd

# 22.12.26
# 2nd try => 실패(시간초과)
# 한 줄의 멀쩡한 사각형을 모두 더하는 방식, 1st보다 느리다
from math import ceil

def solution(w,h):
    answer = w * (h-1)
    
    for y in range(1, h):
        point = ceil(w * y / h)
        answer -= point
        
    return answer * 2

# 3rd try => 16, 18 시간초과
# w, h를 정렬하고 작은 쪽을 for문을 돌면 된다. for문 자체도 적게 돌 수 있도록 신경쓰자. (line 41)
import math

def solution(w,h):
    w, h = max(w,h), min(w,h)
    #gcd
    gcd = math.gcd(w,h)
    small_w = w // gcd
    small_h = h // gcd
    
    #(gcd로 나눈 가장 작은 단위에서) 쓸 수 있는 사각형 개수 연산
    a = small_w / small_h
    can_use = 0
    for i in range(1, small_h):
        can_use += int(a * i)
        
    #(전체 사각형 - 버리는 사각형) 리턴
    return (w * h) - (small_w * h) + (2 * can_use * gcd)


# 4th try => 다른 사람 풀이
import math

def solution(w,h):
    return w * h - (w + h - math.gcd(w,h))
