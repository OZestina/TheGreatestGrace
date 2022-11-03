# https://school.programmers.co.kr/learn/courses/30/lessons/92342

# 1st try
#ryan과 apeach의 점수 계산
def count_point(ryan, apeach):
    r_point = 0
    a_point = 0
    for i in range(11):
        if ryan[i] > apeach[i]: r_point += 10 - i
        elif ryan[i] < apeach[i]: a_point += 10 - i
        else:
            if ryan[i] != 0: a_point += 10 - i
    return r_point - a_point

#같은 점수일 때 더 낮은 점수를 많이 맞힌 경우 찾기
# ryan1 == ryan2 인 경우는 없어서 for문 밖에 return을 별도로 설정하지 않았지만 혹시 모르니 써두는 것도 좋겠다
def less_point(ryan1, ryan2):
    for i in range(10, -1, -1):
        if ryan1[i] > ryan2[i]: return 0
        elif ryan1[i] < ryan2[i]: return 1
# 재귀로 점수와 맞힌 과녁 계산
def recur_arrow(info, n, ryan, idx):
    if idx == 10:
        ryan[idx] = n
        return [count_point(ryan, info), ryan]
    if n == 0:
        return [count_point(ryan, info), ryan]

    temp = ryan[:]
    point, answer = recur_arrow(info, n, temp, idx + 1)
    if info[idx] < n:
        ryan[idx] = info[idx] + 1
        t_point, t_answer = recur_arrow(info, n - ryan[idx], ryan, idx + 1)
        if t_point > point:
            return [t_point, t_answer]
        elif t_point == point:
            if less_point(answer, t_answer):
                return [t_point, t_answer]
            else: return [point, answer]

    return [point, answer]
    
#본체
def solution(n, info):
    ryan = [0,0,0,0,0,0,0,0,0,0,0]
    point, answer = recur_arrow(info, n, ryan, 0)
    
    if point > 0:
        return answer
    return [-1]
