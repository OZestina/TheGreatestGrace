#https://programmers.co.kr/learn/courses/30/lessons/42576

# 1st try => 성공
def solution(participant, completion):
    participant.sort()
    completion.sort()
    result2 = participant[len(participant)-1]
    for i in range(len(participant) -1):
        if participant[i] != completion[i]:
            result2 = participant[i]
            break
    return result2


# 2nd try: 다른 사람의 풀이
# 카운터를 만들어서 뺄 수 있었다..! (카운터 객체는 빼기 가능하지만, 딕셔너리는 불가능하다고 한다)
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# 3rd try: 다른 사람의 풀이 => 해시!
# import할 필요도 없이 그냥 hash(part) 하면 되는거였다! 싱기
def solution(participant, completion):
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
        
    for com in completion:
        temp -= int(hash(com))
    
    return dic[temp]
