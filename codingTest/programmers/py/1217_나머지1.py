# https://programmers.co.kr/learn/courses/30/lessons/87389

import math
def solution(n):
    for i in range(2, math.ceil((n-1)**1/2)):
        if (n-1)%i == 0: return i
    return n-1
  
  
#다른 사람 풀이를 보고 다시 보니, 굳이 math.ceil이나 제곱근을 사용 없이 절반값만 진행하는게 더 낫다고 판단 (제곱근 연산이 복잡)
#(1)보다 (2)의 방법이 연산을 하나 더 줄일 수 있어(n-1) n값이 클수록 더 빠른 처리가 가능하다
def solution(n):
    for i in range(2, (n-1)//2+1):
        # if (n-1)%i == 0: return i     # (1)
        if n%i == 1: return i           # (2)
    return n-1
