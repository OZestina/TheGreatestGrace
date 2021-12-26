# https://programmers.co.kr/learn/courses/30/lessons/12953

# 1st try
# 처음에 가장 큰 값을 최소공배수(answer)로 두고,
# 리스트 중 나눠지지 않는 수(n)만 answer *= n/최대공약수 로 해서 진행
# 최대공약수는 유클리드 호제법으로 진행
def solution(arr):
    answer = max(arr)
    for num in arr:
        a = answer
        n = num
        if a % n:
            while a % n:
                a, n = n, a % n
            answer *= num/n
    return answer
  
  
  
# 2nd try
# 파이썬 math에서 제공하는 최대공약수 함수를 사용해 진행하는 방법 : (import math) math.gcd()
# 1st try보다 변수를 적게쓰고 간단한 코드 완성
# line 30에서 int()처리를 안해주면 'float' object cannot be interpreted as an integer 에러가 뜬다...
# 1st try의 line 15에서는 이런 에러가 안뜨는데 왜일까...
import math
def solution(arr):
    answer = max(arr)
    for num in arr:
        if answer % num:
            answer *= int(num / math.gcd(answer,num))
    return answer


# 3rd try
# 찾아보니까 파이썬 math에는 최소공배수를 리턴하는 함수가 있었다 : (import math) math.lcm()
# 프로그래머스에서는 안되는데, 파이썬 프로그램에서는 돌아가니까 기록!
# 괄호 안에 숫자만 들어가야 하고, 리스트를 바로 넣으면 안돼서 for문으로 진행
import math
def solution(arr):
    answer = 1
    for num in arr:
        answer = math.lcm(answer, num)
    return answer
