# https://school.programmers.co.kr/learn/courses/30/lessons/12938

# 1st try
def solution(n, s):
    answer = []
    t = n
    for _ in range(t):
        new = s // n
        if new == 0:
            return [-1]
        answer.append(new)
        s -= new
        n -= 1
    return answer
  
  
# 2nd try (다른 사람의 풀이 참고)
# 조금 더 수학적인 접근
# s / n의 몫과 나머지를 이용해 몫과 몫+1의 개수를 알아내 
def solution(n, s):
    answer = []
    small = s // n
    if small == 0:
        return [-1]
    for _ in range(n - s%n):
        answer.append(small)
    for _ in range(s%n):
        answer.append(small+1)
    return answer
