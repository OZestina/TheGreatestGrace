# https://school.programmers.co.kr/learn/courses/30/lessons/176962

# 1st try => 성공
def cal_time(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)


def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])
    for i in range(len(plans)):
        plans[i][1] = cal_time(plans[i][1])
    
    queue = []
    remain = dict()
    for i in range(len(plans) - 1):
        time_remain = plans[i+1][1] - plans[i][1]
        #과제 못끝내서 대기 큐로 들어갈 경우
        if int(plans[i][2]) > time_remain:
            queue.append(plans[i][0])
            remain[plans[i][0]] = int(plans[i][2]) - time_remain
            continue
        #시간 같거나 남았을 경우
        answer.append(plans[i][0])
        time_remain -= int(plans[i][2])
        while time_remain and queue:
            if remain[queue[-1]] <= time_remain:
                time_remain -= remain[queue[-1]]
                answer.append(queue.pop())
            else:
                remain[queue[-1]] -= time_remain
                break
        
    answer.append(plans[-1][0])
    while queue:
        answer.append(queue.pop())
    
    return answer
