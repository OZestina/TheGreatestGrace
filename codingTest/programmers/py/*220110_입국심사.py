# https://programmers.co.kr/learn/courses/30/lessons/43238

# 1st try
# 모든 경우의 수를 다 훑는 방법으로 코드 구성 => 역시나 시간초과로 실패
# 이분탐색 문제인데 이 문제를 어떻게 이분탐색으로 풀지?
def solution(n, times):
    #각 심사대 별 걸리는 시간
    need = [0]*len(times)
    #배열 정렬
    times.sort()
    #걸리는 총 시간 & 첫 수 지정
    need[0] = 1
    
    for _ in range(n-1):
        idx = 0
        mini = times[0] * (need[0]+1)
        for i in range(len(times)):
            if times[i] * (need[i]+1) < mini:
                idx = i
                mini = times[i] * (need[i]+1)
        need[idx] += 1
    #걸리는 총 시간 계산
    answer = times[0] * need[0]
    for i in range(len(times)):
        if times[i] * need[i] > answer:
            answer = times[i] * need[i]
    return answer
