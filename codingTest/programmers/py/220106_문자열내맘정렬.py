# https://programmers.co.kr/learn/courses/30/lessons/12915

# 1st try => 성공
def solution(strings, n):
    strings.sort()
    strings.sort(key = lambda a: a[n])
    return strings
  
# 다른 사람의 풀이 참고
# 1) sort 키를 우선순위 순서대로 여러개 줄 수 있다
def solution(strings, n):
    strings.sort(key = lambda a: [a[n],a])
    return strings
  
# 2) 1의 다른 방법
def solution(strings, n):
    strings.sort(key = lambda a: a[n] + a)
    return strings
  
# 3) 한 
def solution(strings, n):
    return sorted(strings, key = lambda a:[a[n],a])
