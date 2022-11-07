# https://school.programmers.co.kr/learn/courses/30/lessons/134240

# 1st try
def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    l = len(answer) - 1
    answer += '0'
    for i in range(l, -1, -1):
        answer += answer[i]
    return answer
