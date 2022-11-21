# https://school.programmers.co.kr/learn/courses/30/lessons/136798


# 1st try
def numofdiv(n, limit, power):
    if n == 1: return 1
    answer = 2
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0: answer += 2
    if int(n**(1/2)) == n**(1/2):
        answer -= 1
    if answer > limit: return power
    return answer

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1):
        answer += numofdiv(i, limit, power)
        
    return answer
  
  
# 2nd try
# n/2의 약수의 개수로 n의 약수의 개수를 구할 수 있는 지 시도해봤는데, 너무 복잡해서 쎄굳바
