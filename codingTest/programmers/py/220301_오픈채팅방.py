# https://programmers.co.kr/learn/courses/30/lessons/42888

# 1st try => 1트만에 성공!
def solution(record):
    nick = dict()   #uid마다 최종 닉네임 저장용
    inouts = []      #들어오고 나간 기록 저장용
    inoutid = []    #들어오고 나간 uid 저장용
    enter = "님이 들어왔습니다."
    exit = "님이 나갔습니다."
    
    for i in record:
        temp = i.split()
        if i[0] == 'E':     #Enter
            nick[temp[1]] = temp[2]
            inouts.append(True)
            inoutid.append(temp[1])
        elif i[0] == 'L':   #Leave
            inouts.append(False)
            inoutid.append(temp[1])
        else:   #Change일 경우
            nick[temp[1]] = temp[2]
    
    answer = []
    for i in range(len(inouts)):
        result = nick[inoutid[i]]
        if inouts[i] == True:
            result += enter
        else:
            result += exit
        answer.append(result)
    
    return answer


# 2nd try (다른 사람 풀이 참고)
# 코드 라인을 더 짧게 줄일 수 있는데, 걸리는 시간 측면에서는 위의 것이 나음
# 시간을 줄이고 싶다면 메모리를 더 써보자
def solution(record):
    nick = dict()   #uid마다 최종 닉네임 저장용
    comment = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    answer = []
    
    for i in record:
        temp = i.split()
        if i[0] == 'E' or i[0] == 'C':     #Enter or Change
            nick[temp[1]] = temp[2]
    
    for i in record:
        temp = i.split()
        if temp[0] != "Change":
            answer.append(nick[temp[1]] + comment[temp[0]])
    
    return answer
