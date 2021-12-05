# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    lost1 = set(lost) - set(reserve)
    reserve1 = set(reserve) - set(lost)
    for i in reserve1:
        if i-1 in lost1:
            lost1 -= set([i-1])
        elif i+1 in lost1:
            lost1 -= set([i+1])
    answer = n - len(lost1)
    return answer
