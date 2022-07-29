# https://programmers.co.kr/learn/courses/30/lessons/12922

#string 값을 더하는 게 + 말고 뭐가 더 없나... 가 기억이 안나서 일단 아래처럼 만듦!

def solution(n):
    a = '수'
    b = '박'
    count = 0
    answer = ''
    while count < n:
        if count%2 ==0:
            answer = answer + a
        else:
            answer = answer + b
        count = count + 1
    return answer
    
# + 만 되는 줄 알았는데, * 도 되더라^^ ( ex. '수박'*2 --> '수박수박')
# 그래서 다시 짠 코드!

def solution(n):
    answer = ''
    answer = n//2 * '수박' + n%2 * '수'
    return answer
    
# 기억합시다! 몫을 구하는 연산자: //, 나머지를 구하는 연사자: %
