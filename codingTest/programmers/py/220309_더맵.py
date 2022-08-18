# https://programmers.co.kr/learn/courses/30/lessons/42626


# 3rd try
# 가장 작은 수를 [0]으로 하는 heap (import heapq) 사용
# 3-1
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            break
        if len(scoville) < 2:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
    return answer


# 3-2
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville) > 1:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
    if scoville[0] < K:
        return -1
    return answer

# ========================================================

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

# 2nd try
# add_spice.sort()을 계속 하는 것 대신 이진정렬로 검색해서 추가하면 하면 더 빠르지 않을까 하여 해봄 => 결과는 동일
def solution(scoville, K):
    answer = 0
    add_spice = []

    for food in scoville:
        if food < K:
            add_spice.append(food)

    over = 0 if len(scoville) == len(add_spice) else 1
    add_spice.sort()

    while len(add_spice) > 1:
        new_sco = add_spice[0] + add_spice[1] * 2
        answer += 1
        add_spice = add_spice[2:]
        if new_sco < K:
            add_spice = insert(add_spice, new_sco)
        else:
            over = 1

    if len(add_spice) == 0:
        return answer
    elif over == 1:
        return answer + 1
    elif over == 0:
        return -1


def insert(foods, new_sco):
    if len(foods) == 0:
        foods.append(new_sco)
        return foods
    pl = 0
    pr = len(foods) - 1
    while True:
        p = (pl + pr) // 2
        if foods[p] == new_sco:
            foods.insert(p, new_sco)
            break
        elif foods[p] > new_sco:
            pr = p - 1
        elif foods[p] < new_sco:
            pl = p + 1
        if pr < pl:
            if pl < len(foods):
                foods.insert(pl, new_sco)
            else: foods.append(new_sco)
            break
    return foods
