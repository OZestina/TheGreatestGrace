# https://school.programmers.co.kr/learn/courses/30/lessons/12985

# 1st try
def solution(n,a,b):
    answer = 0
    while True:               #while a != b: 로도 진행 가능하다 (if문 제외할 수 있음)
        answer += 1
        a = (a+1)//2
        b = (b+1)//2
        if a == b:
            break
    return answer

  
# 다른 사람의 풀이
# xor 비트연산을 이용해 차이 비트의 길이를 구하는 방식. 멋지다!
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
