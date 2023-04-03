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



# (0318 진행내용) ==============================================
#1st try
#틀린 코드는 아닌데, 효율성 테스트 모두 fail...
def solution(participant, completion):
    for i in participant:
        if i in completion:
            completion.remove(i)
        else:
            answer = i
    return answer
  
#2nd
#또 효율성 테스트 모두 fail...
def solution(participant, completion):
    for i in participant:
        try:
            completion.remove(i)
        except:
            answer = i
    return answer

#2-1 try
def solution(participant, completion):
    for i in completion:
        participant.remove(i)
        answer = participant[0]
    return answer
  
#3rd try
#교집합을 이용해서 풀어봤는데, 이건 중복값을 모두 날려버려서 실패.
def solution(participant, completion):
    answer = list (set(participant) - set(completion))
    return answer[0]

#4th try - working on
#카테고리가 '해시'인데, 이걸로 풀어보자....
