# https://school.programmers.co.kr/learn/courses/30/lessons/87390#

#2차원 배열의 좌표값을 이용해 바로 answer를 찾는 방식 => 성공
def solution(n, left, right):
    answer = [i for i in range(left, right + 1)]
    for i in range(len(answer)):
        temp = [answer[i] // n, answer[i] % n]
        answer[i] = max(temp) + 1
    return answer


# answer를 먼저 만들지 않고 바로 저장하는 방법도 있었다
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max([i // n, i % n]) + 1)
    return answer


# 미리 주소값을 다 만들어 두고 값을 바꾸는게 answer가 길때는 더 나은 방법이려나..?
def solution(n, left, right):
    answer = [0] * (right - left + 1)
    for i in range(left, right + 1):
        answer[i - left] = max([i // n, i % n]) + 1
    return answer
