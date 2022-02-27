# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

# 1st try
# combinations과 reduce 익명함수로 시도
# 1번 Timeout으로 실패
from itertools import combinations
from functools import reduce

def solution(clothes):
    closet = dict()
    for item in clothes:
        if item[1] in closet:
            closet[item[1]] += 1
        else:
            closet[item[1]] = 1
    
    answer = 0
    for i in range(1,len(closet.values())+1):
        for combination in combinations(list(closet.values()),i):
            answer += reduce(lambda x,y: x*y, combination)
            
    return answer
  
  
# 2nd try
# 전혀 다른 방식으로 접근했어야 했다
# 각 항목 당 0~n개의 아이템을 착용하는 경우의 수를 곱셈으로 구하고, 모두 착용하지 않는 하나의 수를 빼주는게 제일 빠름...
def solution(clothes):
    closet = dict()
    for item in clothes:
        if item[1] in closet:
            closet[item[1]] += 1
        else:
            closet[item[1]] = 1
    
    answer = 1
    for value in closet.values():
        answer *= value+1
    
    return answer-1
