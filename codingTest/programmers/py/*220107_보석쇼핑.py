# https://programmers.co.kr/learn/courses/30/lessons/67258

# 1st try
# 최소 길이부터 모든 경우의 수를 다 훑는 방법으로 해봄
# 시간초과로 fail
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
  
# 2nd try
# 각 보석의 개수를 세서 1인 애들을 무조건 포함하는 리스트로 시작해야하는걸까..?


def solution(gems):
    gem_list = dict()
    count = 0
    for gem in gems:
        if gem in gem_list:
            gem_list[gem] = gem_list[gem] + [count]
        else: gem_list[gem] = [count]
        count += 1
