# https://school.programmers.co.kr/learn/courses/30/lessons/131129

# 1st try => 런타임 에러 (재귀가 너무 심하게 돈 듯 하다^^;)
def shot(score):
    count, single = score, score
    if score <= 20 or score == 50:
        return [1, 1]
    if score <= 40 and score % 2 == 0:
        return [1, 0]
    if score <= 60 and score % 3 == 0:
        return [1, 0]
    for i in range(2, 21):
        count_i, single_i = shot(score - i)
        if count_i + 1 < count:
            count, single = count_i + 1, single_i + 1
        elif count_i + 1 == count and single < single_i + 1:
            single = single_i + 1
    for i in range(22, 41, 2):
        count_i, single_i = shot(score - i)
        if count_i + 1 < count:
            count, single = count_i + 1, single_i
        elif count_i + 1 == count and single < single_i:
            single = single_i
    for i in range(21, 61, 3):
        count_i, single_i = shot(score - i)
        if count_i + 1 < count:
            count, single = count_i + 1, single_i
        elif count_i + 1 == count and single < single_i:
            single = single_i
    return [count, single]


def solution(target):
    return shot(target)
  
  
# 2nd try (다른 사람의 풀이 참고)
# 이미 계산한 값을 저장하는 메모리를 사용하고(arr), 재귀를 적게 돌도록 1~20 사이에 s, d, t 조건을 걸어줌
# target이 너무 큰 경우 일정 수까지는 60점을 맞췄다고 가정하고 target 자체를 줄이는 방법을 썼더니 마음이 편안...! (line 77)
def shot(score, arr):
    if arr[score]:
        return arr[score]
    
    count, single = score, score
    if score >= 50:
        count, single = shot(score - 50, arr)
        count += 1
        single += 1
    for i in range(1, 21):
        if i > score: break
        temp_c, temp_s = shot(score - i, arr)
        if temp_c + 1 < count:
            count, single = temp_c + 1, temp_s + 1
        elif temp_c + 1 == count and single < temp_s + 1:
            single = temp_s + 1
        
        if i * 2 <= score:
            temp_c, temp_s = shot(score - i * 2, arr)
            if temp_c + 1 < count:
                count, single = temp_c + 1, temp_s
            elif temp_c + 1 == count and single < temp_s:
                single = temp_s
            
        if i * 3 <= score:
            temp_c, temp_s = shot(score - i * 3, arr)
            if temp_c + 1 < count:
                count, single = temp_c + 1, temp_s
            elif temp_c + 1 == count and single < temp_s:
                single = temp_s
    
    return [count, single]


def solution(target):
    
    count = 0
    while target > 500:
        target -= 60
        count += 1
    
    arr = [[] for _ in range(target + 1)]
    arr[0] = [0, 0]
    
    for i in range(1, target + 1):
        if i < 21 or i == 50: arr[i] = [1, 1]
        elif i < 41 and i % 2 == 0: arr[i] = [1, 0]
        elif i < 61 and i % 3 == 0: arr[i] = [1, 0]
        else:
            arr[i] = shot(i, arr)
    
    return [arr[target][0] + count, arr[target][1]]
