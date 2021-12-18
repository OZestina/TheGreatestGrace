# https://programmers.co.kr/learn/courses/30/lessons/12899#

#1st try
#n을 3, 3^2, 3^3...으로 나눈 나머지를 가지고 계산하는 방법을 생각함
#숫자로 answer에 저장해서 for문 & str(숫자) 로 했더니 효율성 테스트에서 낙제
#   => 아예 저장을 문자로하고, join하는 방법으로 성공

def solution(n):
    answer = []
    divisor = 3
    while n > 0:
        remainder = n % divisor
        if remainder == 0:
            answer.append('4')
            n -= divisor
        elif remainder == divisor/3:
            answer.append('1')
            n -= remainder
        else:
            answer.append('2')
            n -= remainder
        divisor *= 3
    return "".join(reversed(answer))
  
  
#2nd try
#계속 3으로 나눠어서 하는 방법...
#훨씬 간단하고 3의 제곱수로 나누는것보다 연산이 쉬울 것이기에 더 낫다

def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 0:
            answer += '4'
            n = n // 3 - 1
        elif n % 3 == 1:
            answer += '1'
            n = n // 3
        elif n % 3 == 2:
            answer += '2'
            n = n // 3
    return "".join(reversed(answer))
