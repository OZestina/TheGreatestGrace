# https://school.programmers.co.kr/learn/courses/30/lessons/42628

# 1st try
def insert(q, n:int):
    end = len(q) - 1
    start = 0
    
    if end == -1 or q[end] < n:
        q.append(n)
    else:
        while start <= end:
            check = (end + start) // 2
            if q[check] < n:
                start = check + 1
            elif q[check] > n:
                end = check - 1
            else:
                break
        q.insert(check, n)

        
def solution(operations):
    q = []
    
    for oper in operations:
        if oper.startswith("I"):
            insert(q, int(oper[2:]))
        elif oper[2] == "-":
            if len(q) != 0:
                q.pop(0)
        else:
            if len(q) != 0:
                q.pop()
            
    if len(q) == 0:
        return [0,0]
    return [max(q), min(q)]
