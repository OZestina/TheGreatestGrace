# https://school.programmers.co.kr/learn/courses/30/lessons/172927

# 1st try
def get_weight(mineral):
    if mineral[0] == "d":
        return 100
    elif mineral[0] == "i":
        return 10
    return 1
    
    
def get_stress(p_i, work):
    s_work = '00' + str(work)
    if p_i == 0: #다이아 곡괭이
        return int(s_work[-3]) + int(s_work[-2]) + int(s_work[-1])
    elif p_i == 1: #철 곡괭이
        return int(s_work[-3]) * 5 + int(s_work[-2]) + int(s_work[-1])
    else:
        return int(s_work[-3]) * 25 + int(s_work[-2]) * 5 + int(s_work[-1])
    

def solution(picks, minerals):
    # 사용하는 총 작업량(곡괭이 수) 계산 (total_shift)
    len_min = len(minerals)
    total_shift = min(sum(picks), (len_min - 1) // 5 + 1)
    
    # 한 작업 당 weight 계산 (추후 계산 편의를 위해 100, 10, 1로 지정)
    total_weight = []
    weight = 0
    for i in range(len_min):
        weight += get_weight(minerals[i])
        if i % 5 == 4:
            total_weight.append(weight)
            weight = 0
            if i // 5 + 1 == total_shift:
                break
    if weight:
        total_weight.append(weight)
    
    # 작업 weight sort해 작업량 높은 순부터 비싼 곡괭이 사용
    answer = 0
    p_i = 0
    for work in sorted(total_weight, reverse=True):
        while not picks[p_i]:
            p_i += 1
        answer += get_stress(p_i, work)
        picks[p_i] -= 1
        
    
    return answer
