# https://programmers.co.kr/learn/courses/30/lessons/12945

# 1st try
# 정석(?)인 재귀함수 => 런타임 에러 발생
def solution(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return (solution(n-1) + solution(n-2)) % 1234567
    
    
# 2nd try
