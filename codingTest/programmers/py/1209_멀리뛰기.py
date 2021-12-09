# https://programmers.co.kr/learn/courses/30/lessons/12914

#피보나치 수열
def solution(n):
    q = [1,2]
    if n == 1: return 1
    elif n == 2: return 2
    else:
        for i in range(n-2):
            q.append((q[i]+q[i+1])%1234567)
        return q[len(q)-1]
      
      
# 다른 사람 풀이보고 가져온 것
# 메모리도 적게쓰고 (배열 필요없음), 시간도 더 빠르다!
def solution(n):
    if n == 1: return 1
    elif n == 2: return 2
    else:
        a, b = 1, 2
        for i in range(2,n):
            a, b = b, (a+b)%1234567
        return b
