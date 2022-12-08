# https://school.programmers.co.kr/learn/courses/30/lessons/140108?language=python3

def solution(s):
    answer = 0
    first = 0
    count = [0, 0]
    
    for i in range(len(s) - 1):
        if s[i] == s[first]: count[0] += 1
        else: count[1] += 1
        if count[0] == count[1]:
            answer += 1
            count[0], count[1] = 0, 0
            first = i + 1
            
    return answer + 1
