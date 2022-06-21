# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    total = brown + yellow
    for i in range(2, (total+1)//2):
        if total % i == 0:
            if (i - 2) * (total/i - 2) == yellow:
                return [total/i, i]
