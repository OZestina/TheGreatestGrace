# https://school.programmers.co.kr/learn/courses/30/lessons/12979#


# 1st try
def solution(n, stations, w):
    answer = 0

    current = 1
    max_range = 2 * w + 1
    #1부터 station으로 커버되는 부분 확인
    for s in stations:
        s_s, s_e = s - w, s + w
        if current < s_s:
            while current < s_s:
                answer += 1
                current += max_range
        if s_s <= current <= s_e:
            current = s_e + 1
        if n < current:
            break
            
    if n < current:
        return answer
    #station으로 커버 안되는 그 이후 부분 확인
    while current <= n:
        answer += 1
        current += max_range
    return answer
  
  
# 2nd try (다른 사람 풀이 참고)
# (커버되는 아파트를 나머지로 버리면서) 커버해야 하는 거리를 나누어서 기지국 수를 계산하는 방법. 빠르다
def solution(n, stations, w):
    answer = 0

    before = -w
    cover = 2 * w + 1
    for s in stations:
        answer += (s - before - 1) // cover
        before = s
        
    return answer + (n + w - before) // cover
