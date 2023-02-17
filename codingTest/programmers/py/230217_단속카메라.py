# https://school.programmers.co.kr/learn/courses/30/lessons/42884#

# 1st try => 효율성 3/5
# 정말 정말 greedy
def max_car(routes, idx, pos_cam, l):
    count = idx + 1
    while count < l:
        if routes[count][0] <= pos_cam <= routes[count][1]:
            count += 1
        else:
            break
    return count
    

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0])
    l = len(routes)
    
    idx = 0
    while idx < l:
        count = 0
        for pos_cam in range(routes[idx][0], routes[idx][1] + 1):
            count = max(max_car(routes, idx, pos_cam, l), count)
        idx = count
        answer += 1
    
    return answer

  
# 2nd try
# 기준점이 되는 차량을 감시하면서 다음 차량을 감시할 수 있는지 확인하는 구간을 start, end로만 처리해 연산속도 업!
def next_cam(routes, idx, l):
    start, end = routes[idx][0], routes[idx][1]
    
    count = idx + 1
    while count < l:
        n_start, n_end = routes[count][0], routes[count][1]
        if end < n_start or n_end < start:
            break
        end = min(end, n_end)
        start = max(start, n_start)
        count += 1
    return count


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0])
    l = len(routes)
    
    idx = 0
    while idx < l:
        idx = next_cam(routes, idx, l)
        answer += 1
    
    return answer
  
  
# 3rd try (다른 사람 풀이)
# x[1]을 기준으로 정렬하면 가장 마지막 지점에 카메라를 세우고 그 카메라가 몇 대의 차량을 커버하는지 계산할 수 있게 된다. super fast!
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30001
    
    answer = 0
    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer
