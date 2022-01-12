# https://programmers.co.kr/learn/courses/30/lessons/12936

# 1st try
# 팩토리얼은 math.factorial(숫자)로 사용
# 리스트에서 .pop(idx)로 해당 인덱스의 값을 pop할 수 있다
from math import factorial

def solution(n, k):
    ppl = [i+1 for i in range(n)]
    # ppl = list(range(1,n+1)) 로 해도 된다
    answer = []
    dividend = k-1
    
    for i in range(n-1):
        divisor = factorial(n-1-i)
        # 몫이 인덱스가 된다
        answer.append(ppl.pop(dividend // divisor))
        # 나머지는 새로운 피제수가 된다
        dividend = dividend % divisor
    
    # n-1번만 연산하고, 가장 마지막 것은 별도로 추가. for문을 n번 연산하고 line 20 지워도 돌아간다
    answer.append(ppl[0])
    return answer
  
  
# 2nd try
# 1) 배열의 인덱스 값으로는 "(k-1)//a"와 "(k//a)-1"이 같아서 하나로 합쳐줄 수도 있었다
#      => [배열길이-1] == [-1] : 가장 마지막 항목
# 2) m, n = a, b 로 하면 간편하다
from math import factorial

def solution(n, k):
    ppl = list(range(1,n+1))
    answer = []
    
    for i in range(n):
        answer.append(ppl.pop((k-1) // factorial(n-1)))
        k, n = k % factorial(n-1), n-1
    return answer
