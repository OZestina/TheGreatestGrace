# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    s = [int(i) for i in s.split()]
    answer = str(min(s)) + ' ' + str(max(s))
    return answer
