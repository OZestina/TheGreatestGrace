# https://school.programmers.co.kr/learn/courses/30/lessons/152996#

# 1st try
from collections import Counter

def siso_pair(n1, n2):
    if n1 == n2: return 1
    
    temp = n1 / n2
    if temp == 0.5: return 1
    if temp == 2 / 3: return 1
    if temp == 3 / 4: return 1
    return 0

def solution(weights):
    answer = 0
    
    dic = Counter(weights)
    dic_item = list(dic.keys())
    l = len(dic)
    for i in range(l - 1):
        for j in range(i + 1, l):
            small = dic_item[i]
            big = dic_item[j]
            if big < small:
                small, big = big, small
            answer += siso_pair(small, big) * dic[small] * dic[big]
    #같은 값끼리 묶어서 계산
    for k in dic:
        value = dic[k]
        if value > 1:
            answer += value * (value - 1) // 2
        
    return answer
  
  
  
# 2nd try (다른 사람 풀이 참고)
# 기준 값을 두고 비율(ratio)을 곱한 값이 dic에 있는지 확인하는 방법으로 하면 연산이 
from collections import Counter

def solution(weights):
    answer = 0

    dic = Counter(weights)
    dic_item = list(dic.keys())
    l = len(dic)
    ratio = [2, 3 / 2, 4 / 3]
    
    for weight in dic_item:
        if dic[weight] > 1:
            answer += dic[weight] * (dic[weight] - 1) // 2
        for r in ratio:
            answer += dic[weight * r] * dic[weight]
    
    return answer
