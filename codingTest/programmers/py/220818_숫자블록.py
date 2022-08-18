# https://school.programmers.co.kr/learn/courses/30/lessons/12923?language=python3#

def great_devisor(n):
    if n == 1:
        return 0
    if n % 2 == 0 and n <= 20000000:
        return n // 2
    result = 1
    for i in range(3, int(n**(1/2)) + 1):
        if n % i == 0:
            devisor = n // i
            if devisor <= 10000000:
                return devisor
    return result

def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        answer.append(great_devisor(i))
    return answer
