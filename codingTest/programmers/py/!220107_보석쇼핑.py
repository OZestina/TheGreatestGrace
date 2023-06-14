# https://programmers.co.kr/learn/courses/30/lessons/67258

# 1st try (시간초과 fail)
# 최소 길이부터 모든 경우의 수를 다 훑는 방법으로 해봄
def solution(gems):
    gem_len = len(set(gems))
    length = gem_len
    while length > 0:
        for idx in range(len(gems)-gem_len+1):
            if gem_len <= len(set(gems[idx:idx+length])):
                answer = [idx+1, idx+length]
                length = -2
                break
        length += 1
    return answer
  

# 2nd try (23.02.22) (효율성 fail)
from collections import defaultdict

def solution(gems):
    answer = []
    
    jewel = defaultdict(list)
    for i in range(len(gems)):
        jewel[gems[i]] += [i]
    
    for i in range(len(gems)):
        end = i
        for j, value in jewel.items():
            if value[-1] < i:
                end = -1
                break
            for v in value:
                if i <= v:
                    if end < v:
                        end = v
                    break
        if i <= end:
            answer.append([i, end])
        
    temp = min(answer, key=lambda x: x[1] - x[0])
    return [temp[0] + 1, temp[1] + 1]


# 3rd try (23.06.14) =====================================================================
# 각 시작점에서 시작하는 보석을 모두 포함하는 리스트를 기준으로 left_idx(start), right_idx(last) 조정하며 탐색
# 보석이 모두 모였는 지를 필요할 때마다 딕셔너리 전체 탐색이 아닌 별도 변수(empty)로 저장해 바로 확인할 수 있게 했더니 통과
def solution(gems):
    #gem의 종류를 기억할 jewel 딕셔너리 생성 & gem 목록 정리
    jewel = dict()
    for g in gems:
        jewel[g] = 0
        
    #리턴값(answer)초기화
    len_g = len(gems)
    answer = [0, len_g]
    
    last = 1
    jewel[gems[0]] += 1
    empty = len(jewel) - 1  #모아야하는 보석 수 (0이면 모두 모임)
    
    #gems 순회하면서 진행
    for start in range(len_g):
        while last < len_g and empty:
            if jewel[gems[last]] == 0:
                empty -= 1
            jewel[gems[last]] += 1
            last += 1
            
        #보석 다 모았으면 answer 보다 길이가 짧은 지 확인 후 업데이트
        if empty == 0:
            if answer[1] - answer[0] > last - start:
                answer = [start, last]

        if jewel[gems[start]] == 1:
            empty += 1
        jewel[gems[start]] -= 1
        
    
    return [answer[0] + 1, answer[1]]
