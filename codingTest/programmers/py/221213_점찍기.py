# https://school.programmers.co.kr/learn/courses/30/lessons/140107

# 1st try => 시간초과
# 이중 for문으로 모든 점마다 연산을 하려고 했으니 불필요한 연산이 많았다
def solution(k, d):
    answer = 0
    same = 0
    for a in range(0, d+1):
        for b in range(a, d+1):
            if d**2 < (a*k)**2 + (b*k)**2:
                break
            elif a == b:
                same += 1
            else:
                answer += 1
    return answer * 2 + same
  
  
# 2nd try
# x좌표를 기준으로 가능한 y좌표의 개수를 세는 방식으로 진행
# (3rd에서 본 내용) line 26의 int()처리는 해주지 않아도 된다
def solution(k, d):
    answer = 0
    
    for a in range(0, d + 1, k):
        b = (d**2 - a**2)**0.5        # b = int((d**2 - a**2)**0.5)
        answer += b // k + 1
        
    return answer
  
  
# 3rd try (다른 사람의 풀이)
# 대략적인 내용은 2nd와 비슷하나, x == 0인 점을 별도로 계산해 준 점이 인상깊다.
# 근데 이게 더 느리다고 나오네용
def solution(k, d):
    c = 0
    for y in range(0, d, k):
        x = (d**2 - y**2)**0.5
        c += x//k
    return c + d//k + 1
