# https://school.programmers.co.kr/learn/courses/30/lessons/150369#

# 1st try
# 택배를 가장 먼 곳부터 배달하는 거리와 가장 먼 곳부터 수거하는 거리를 비교해 더 먼 곳을 answer에 더하는 방식으로 진행
def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d_idx = n - 1
    p_idx = n - 1
    
    while d_idx > -1 or p_idx > -1:
        temp_d, temp_p = -1, -1
        bag = cap
        for i in range(d_idx, -1, -1):
            if deliveries[i] == 0:
                continue
            if bag == cap:
                temp_d = i
            if deliveries[i] <= bag:
                bag -= deliveries[i]
                deliveries[i] = 0
                d_idx = i - 1
            else:
                deliveries[i] -= bag
                bag = 0
                d_idx = i
            if bag == 0:
                break
        if i == 0 and deliveries[i] == 0:
            d_idx = -1
        
        bag = cap
        for i in range(p_idx, -1, -1):
            if pickups[i] == 0:
                continue
            if bag == cap:
                temp_p = i
            if pickups[i] <= bag:
                bag -= pickups[i]
                pickups[i] = 0
                p_idx = i - 1
            else:
                pickups[i] -= bag
                bag = 0
                p_idx = i
            if bag == 0:
                break
        if i == 0 and pickups[i] == 0:
            p_idx = -1
        
        if temp_d > temp_p: answer += (temp_d + 1) * 2
        else:               answer += (temp_p + 1) * 2

        
    return answer
  
  
# 2nd try (다른 사람 풀이 참고)
def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0
    for i in range(n - 1, -1, -1):
        if deliveries[i] or pickups[i]:
            pos = i
            break

    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        while d > cap or p > cap:
            d -= cap
            p -= cap
            answer += 2 * (pos + 1)
            pos = i

    if d > 0 or p > 0:
        answer += 2 * (pos + 1)

    return answer

