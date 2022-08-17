# https://school.programmers.co.kr/learn/courses/30/lessons/87390#

#2차원 배열의 좌표값을 이용해 바로 answer를 찾는 방식 => 성공

def solution(n, left, right):
    answer = [i for i in range(left, right + 1)]
    for i in range(len(answer)):
        temp = [answer[i] // n, answer[i] % n]
        answer[i] = max(temp) + 1
    return answer
