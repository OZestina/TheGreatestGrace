# https://school.programmers.co.kr/learn/courses/30/lessons/12924

# 1st try
# 모든 경우의 수 확인
def start_total(i, n):
    result = n
    for num in range(i, n):
        result -= num
        if result == 0:
            return 1
        elif result < 0:
            return 0

def solution(n):
    answer = 1
    for i in range(1, n//2 + 1):
        if start_total(i, n) == 1:
            answer += 1
    return answer
  
  
# 2nd try
# 약수 중 홀수의 개수
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 1:
            answer += 1
    return answer
  
# 3rd try
# 약수 구할 때 짝을 찾아 바로 홀수인지 확인하면 시간이 더 줄어든다
def solution(n):
    answer = 0
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            if i % 2 == 1:
                answer += 1
            if i != n//i and n//i % 2 == 1:
                answer += 1
    return answer
