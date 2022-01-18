# https://programmers.co.kr/learn/courses/30/lessons/42889

# 1st try => 성공
def solution(N, stages):
    #각 유저의 위치 확인
    users_at = [0]*(N+1)
    for stage in stages:
        users_at[stage-1] += 1
    #각 스테이지 별 실패율 계산
    fail_rate = [0]*N
    reached = len(stages)
    for stage in range(N):
        fail_rate[stage] = users_at[stage] / reached
        reached -= users_at[stage]
        if reached == 0: break
    #실패율 높은 스테이지 순으로 리스트 업
    answer = []
    for _ in range(N):
        max_idx = fail_rate.index(max(fail_rate))
        answer.append(max_idx+1)
        fail_rate[max_idx] = -1
    return answer
  
# 2nd try (다른 사람의 풀이 참고)
# 각 유저의 위치를 저장하는 for문에서 N+2 길이의 리스트로 +-1 연산 없앰 => len(stages) 만큼의 +연산이 줄어듦
# 실패율 높은 순으로 정렬 및 stage 레벨 저장하는 방법에서 간결하고 연산이 적은 방식 사용
#   => 1) fail_rate(실패율)을 (레벨, 실패율)로 저장
#   => 2) fail_rate 각 항목의 [1]번을 기준으로 reverse 정렬해서 진행
def solution(N, stages):
    #각 유저의 위치 확인
    users_at = [0] * (N + 2)
    for stage in stages:
        users_at[stage] += 1
    #각 스테이지 별 실패율 계산
    fail_rate = [None] * N
    reached = len(stages)
    for i in range(N):
        if reached == 0:
            fail_rate[i] = (i+1, 0)
            continue
        fail_rate[i] = (i+1, users_at[i+1] / reached)
        reached -= users_at[i+1]
    #실패율 높은 순으로 정렬해 stage 레벨 저장
    answer = []
    for stage in sorted(fail_rate, key=lambda x: x[1], reverse=True):
        answer.append(stage[0])
    return answer
