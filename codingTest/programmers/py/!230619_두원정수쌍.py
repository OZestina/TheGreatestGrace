# https://school.programmers.co.kr/learn/courses/30/lessons/181187#

# 1st try
# y축만 포함하는 1사분면의 정수 개수를 구해 4배해서 리턴
import math

def solution(r1, r2):
    answer = 0
    
    # 1사분면(+ 축 하나)만 검사 후 4배 하자
    for y in range(1, r2 + 1):
        pos_r1, pos_r2 = 0, (r2**2 - y**2)**(1/2)
        if r1 >= y : pos_r1 = (r1**2 - y**2)**(1/2)
        answer += math.floor(pos_r2) - math.ceil(pos_r1) + 1
    
    return answer * 4
