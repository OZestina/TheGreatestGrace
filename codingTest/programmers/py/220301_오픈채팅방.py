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
