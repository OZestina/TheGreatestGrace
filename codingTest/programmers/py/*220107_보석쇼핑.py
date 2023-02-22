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
