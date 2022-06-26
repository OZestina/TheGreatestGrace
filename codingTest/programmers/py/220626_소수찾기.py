# https://programmers.co.kr/learn/courses/30/lessons/42839

# 1st try => 성공
# 파이썬 내장 기능인 순열(permutations)을 이용
from itertools import permutations

def check_prime(str_n):
    n = int(str_n)
    if n < 2:
        return 0
    if n == 2:
        return n
    if n % 2 == 0:
        return 0
    for i in range(3, int(n**(1/2))+1):
        if n % i == 0:
            return 0
    return n

def solution(numbers):
    length = len(numbers)
    answer = 0
    prime = []
    
    for i in range(1, length+1):
        arrs = list(permutations(numbers, i))
        for arr in arrs:
            n = check_prime(''.join(list(arr)))
            if n != 0 and n not in prime:
                prime.append(n)
                answer += 1
    return answer
  

  
# 2nd try (다른 사람의 풀이 참고)
# 배운 것
#   1) set()를 사용해 중복 수 제거
#   2) | (합집합 연산자)를 |= 로 사용할 수 있다..!
#   3) 코드는 간결하지만 연산속도는 느리다
from itertools import permutations

def solution(numbers):
    prime = set()
    for i in range(len(numbers)):
        prime |= set(map(int, map("".join, permutations(numbers, i+1))))
    prime -= set(range(0,2))
    for i in range(2, int(max(prime)**(1/2))+1):
        prime -= set(range(i*2, max(prime)+1, i))
    return len(prime)
