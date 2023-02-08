# https://school.programmers.co.kr/learn/courses/30/lessons/135807#

# 1st try
def gcd(n1, n2):    #최대공약수 구하기
    if n1 < n2: n1, n2 = n2, n1
    while n1 % n2 != 0:
        n1, n2 = n2, n1 % n2
    return n2


def solution(arrayA, arrayB):
    answer = 0
    gcdA, gcdB = arrayA[0], arrayB[0]
    
    for i in range(1, len(arrayA)):
        gcdA = gcd(arrayA[i], gcdA)
        gcdB = gcd(arrayB[i], gcdB)
    
    for b in arrayB:
        if b % gcdA == 0:
            break
    else:
        answer = gcdA
    
    for a in arrayA:
        if a % gcdB == 0:
            break
    else:
        answer = max(answer, gcdB)
    
    return answer  
  
  
  
  
# 2nd try (다른 사람 풀이)
# gcd 직접구현보다 math.gcd가 더 빠르다.
# reduce() 로 gcd 구하는게 더 빠르다.
# 어려운 문제는 아니었는데, 괜히 어렵게 생각해서 빙빙 돌았다...

from math import gcd
from functools import reduce

def check(arrayA, arrayB):
    gcd_A = reduce(gcd, arrayA, arrayA[0])
    if all(i % gcd_A for i in arrayB):
        return gcd_A
    return 0

def solution(arrayA, arrayB):
    return max(check(arrayA, arrayB), check(arrayB, arrayA))
