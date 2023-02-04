# https://school.programmers.co.kr/learn/courses/30/lessons/67257

# 1st try
def calculate(oper, i):
    if i == 0:   prior = "+-*"
    elif i == 1: prior = "+*-"
    elif i == 2: prior = "-+*"
    elif i == 3: prior = "-*+"
    elif i == 4: prior = "*+-"
    else:        prior = "*-+"
    
    to_remove = []
    for p in prior:
        for o in range(len(oper)):
            if oper[o] == p:
                oper[o + 1] = eval(str(oper[o-1]) + oper[o] + str(oper[o+1]))
                to_remove += [o-1, o]
        for t in reversed(to_remove):
            oper.pop(t)
        to_remove = []
    
    return int(oper[0])
    

def solution(expression):
    answer = []
    
    oper = []
    start = 0
    for i in range(len(expression)):
        if expression[i] in "-+*":
            oper.append(expression[start:i])
            oper.append(expression[i])
            start = i + 1
    oper.append(expression[start:])
    
    for i in range(6):
        answer.append(abs(calculate(oper[:], i)))
    
    return max(answer)
