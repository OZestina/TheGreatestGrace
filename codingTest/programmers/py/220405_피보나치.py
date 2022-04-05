# https://programmers.co.kr/learn/courses/30/lessons/12945

# 1st try
# 정석(?)인 재귀함수 => 런타임 에러 발생
def solution(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return (solution(n-1) + solution(n-2)) % 1234567
    
    
# 2nd try
# 재귀포기, for문으로 O(n) 복잡도 코드로 작성 => 성공
def solution(n):
    F = [0,1] + [0]*(n-1)
    for i in range(2, n+1):
        F[i] = (F[i-1] + F[i-2]) % 1234567
    return F[n]



# 3rd try: 다른 사람의 풀이 참고
# 맞다 맞다 for문 없이 이렇게 할 수도 있었지!
def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, (a+b)%1234567
    return a
