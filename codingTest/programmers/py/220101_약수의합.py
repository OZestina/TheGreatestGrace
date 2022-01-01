# https://programmers.co.kr/learn/courses/30/lessons/12928#

# 1st try
def solution(n):
    answer = 0
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            answer += i
            if n//i != i:
                answer += n//i    
    return answer
  
  
# 2nd try
# 제곱근이 약수일 때를 별도로 빼줄 수도 있는데, 효율 측면에서 별 차이는 없는듯하다
def solution(n):
    answer = 0
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            answer += i
            answer += n//i    
    if n**(1/2) == int(n**(1/2)):
        answer -= n**(1/2)
    return answer
  
  
# 3nd try
# (코드를) 더 간단하게 이렇게 할 수도 있는데 실행속도에서는 1st가 나음
def solution(n):
    answer = n
    for i in range(1, n//2+1):
        if n % i == 0:
            answer += i
    return answer
  
