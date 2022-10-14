# https://school.programmers.co.kr/learn/courses/30/lessons/131128

# 1st try
def solution(X, Y):
    dupl = []
    for n in "0123456789":
        if n in X and n in Y:
            howmany = min(X.count(n), Y.count(n))
            for i in range(howmany):
                dupl.append(n)
    
    dupl = sorted(dupl, reverse=True)
    if len(dupl) == 0:
        return "-1"
    
    answer = "".join(sorted(dupl, reverse=True))
    if answer[0] == "0":
        return "0"
    return answer
  
  
# 2nd try (다른 사람의 풀이)
# sort를 제외하는 방식. 훨씬 빠르다

def solution(X, Y):
    x_count = [X.count(i) for i in "0123456789"]
    y_count = [Y.count(i) for i in "0123456789"]
    
    answer = ''
    for i in range(9, -1, -1):
        answer += str(i) * min(x_count[i], y_count[i])
    
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    return answer
