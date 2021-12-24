# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = len(d)
    d.sort()
    total = sum(d)
    while total > budget:
        total -= d[answer-1]
        answer -= 1
    return answer
  
# 다른 사람의 풀이를 보니, 같은 생각의 코드를 더 쉽게 쓴 게 있어서 공부
# 굳이 answer, total 변수를 안만들어도 되는 것이었다! (len(d)는 마지막에 한 번만 해도 된다)
def solution(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()
    return len(d)
