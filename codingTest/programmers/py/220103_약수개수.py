# https://programmers.co.kr/learn/courses/30/lessons/77884/solution_groups?language=python3

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if num**(0.5) == int(num**(0.5)):
            answer -= num
        else: answer += num
    return answer
