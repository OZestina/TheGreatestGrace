# https://programmers.co.kr/learn/courses/30/lessons/42626

# 1st try
# 정확성은 pass, 효율성은 모두 fail
def solution(scoville, K):
    answer = 0
    add_spice = []
    
    for food in scoville:
        if food < K:
            add_spice.append(food)
            
    over = 0 if len(scoville) == len(add_spice) else 1
    
    while len(add_spice) > 1:
        add_spice.sort()
        new_sco = add_spice[0] + add_spice[1]*2
        answer += 1
        add_spice = add_spice[2:]
        if new_sco < K:
            add_spice += [new_sco]
            
        else:
            over = 1
    
    if len(add_spice) == 0:
        return answer
    elif over == 1:
        return answer + 1
    elif over == 0:
        return -1
