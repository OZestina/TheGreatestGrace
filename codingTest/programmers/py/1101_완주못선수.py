#https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()
    result2 = participant[len(participant)-1]
    for i in range(len(participant) -1):
        if participant[i] != completion[i]:
            result2 = participant[i]
            break
    return result2
