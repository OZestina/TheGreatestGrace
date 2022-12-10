# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    letters = dict()
    
    for i in range(len(s)):
        if s[i] in letters:
            answer.append(i - letters[s[i]])
        else:
            answer.append(-1)
        letters[s[i]] = i
    
    return answer
