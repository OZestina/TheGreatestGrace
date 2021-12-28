# https://programmers.co.kr/learn/courses/30/lessons/42586


# 1st try
# 머릿속으로 이렇게 이렇게 하면 되지 않을까? 해서 해본게 1트만에 성공!
import math

def solution(progresses, speeds):
    answer = []
    process = 1
    day = -1
    for process_num in range(len(progresses)-1):
        if day == -1:
            day = math.ceil((100 - progresses[process_num]) / speeds[process_num])
            process = 1
        elif speeds[process_num] * day + progresses[process_num] >= 100:
            process += 1
        else:
            answer.append(process)
            process = 1
            day = math.ceil((100 - progresses[process_num]) / speeds[process_num])
    if speeds[len(speeds)-1] * day + progresses[len(speeds)-1] >= 100:
        answer.append(process+1)
    else:
        answer.append(process)
        answer.append(1)
    return answer
  
  
# 2nd try
# 다른 사람의 풀이를 보다가 발견한 내용으로 수정^^
# 1) day 초기값을 첫 day값으로 지정해서 if문 하나 없애기
# 2) 마지막 프로세스를 별도 if문으로 안빼고 answer.append(process)로 진행
import math

def solution(progresses, speeds):
    answer = []
    process = 0
    day = math.ceil((100 - progresses[0]) / speeds[0])
    for process_num in range(len(progresses)):
        if speeds[process_num] * day + progresses[process_num] >= 100:
            process += 1
        else:
            answer.append(process)
            process = 1
            day = math.ceil((100 - progresses[process_num]) / speeds[process_num])
    answer.append(process)
    return answer
