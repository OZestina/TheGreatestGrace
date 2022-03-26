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
