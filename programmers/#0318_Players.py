#https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

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
