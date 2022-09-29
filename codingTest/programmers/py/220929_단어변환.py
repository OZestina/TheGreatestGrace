# https://school.programmers.co.kr/learn/courses/30/lessons/43163#

# 1st try
def diffletter(target, words):
    for word in words:
        flag = 0
        for i in range(len(target)):
            if target[i] != word[i]:
                flag += 1
        if flag == 1:
            return 1
    return 0


def solution(begin, target, words):
    n = len(words)
    answer = [-2 for i in words]
    for i in range(n):
        if words[i] == target and diffletter(begin, words[i:i+1]) == 1:
            return 1
        elif words[i] == target:
            answer[i] = 0
        elif diffletter(begin, words[i:i+1]) == 1:
            answer[i] = -1
    if 0 not in answer or -1 not in answer:
        return 0
    
    distance = 0
    tocheck = [target]
    while len(tocheck) > 0:
        temp = []
        for i in range(n):
            if answer[i] == -1:
                if diffletter(words[i], tocheck) == 1:
                    return distance + 2
            elif answer[i] == -2:
                if diffletter(words[i], tocheck) == 1:
                    answer[i] = distance + 1
                    temp.append(words[i])
        
        tocheck = temp
        distance += 1
        
    return 0


