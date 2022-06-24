# https://programmers.co.kr/learn/courses/30/lessons/77485

# 1st try => 성공
# 역으로 돌면서 덮어쓰는 방식으로 진행
def solution(rows, columns, queries):
    #create template
    template = []
    for i in range(rows):
        template.append([columns*i + j + 1 for j in range(columns)])
    #proceed queries
    answer = []
    for query in queries:
        for i in range(len(query)):
            query[i] -= 1
        x1, y1, x2, y2 = query
        mini = temp = template[x1][y1]
        for i in range(x1, x2):
            template[i][y1] = template[i+1][y1]
            if template[i+1][y1] < mini:
                mini = template[i+1][y1]
        for i in range(y1, y2):
            template[x2][i] = template[x2][i+1]
            if template[x2][i+1] < mini:
                mini = template[x2][i+1]
        for i in range(x2, x1, -1):
            template[i][y2] = template[i-1][y2]
            if template[i-1][y2] < mini:
                mini = template[i-1][y2]
        for i in range(y2, y1, -1):
            template[x1][i] = template[x1][i-1]
            if template[x1][i-1] < mini:
                mini = template[x1][i-1]
        template[x1][y1+1] = temp
        if temp < mini:
            mini = temp
        answer.append(mini)
    return answer
  
  
  
# 2nd try (다른 사람의 풀이 참고)
# 바꿔야 하는 숫자를 모두 저장해두고 rotate 시켜서 다시 덮어쓰는 방법
# 자가로 진행했지만 deque.rotate()로도 진행이 가능하다고 한다 => 3rd try
def solution(rows, columns, queries):
    #create template
    template = [[columns*i + j + 1 for j in range(columns)] for i in range(rows)]
    
    #proceed queries
    answer = []
    for query in queries:
        #position setting
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        #saving num
        num = []
        for i in range(y1, y2):
            num.append(template[x1][i])
        for i in range(x1, x2):
            num.append(template[i][y2])
        for i in range(y2, y1, -1):
            num.append(template[x2][i])
        for i in range(x2, x1, -1):
            num.append(template[i][y1])
        #saving min num
        answer.append(min(num))
        #rotate num
        num.insert(0, num.pop())
        #new num append
        for i in range(y1, y2):
            template[x1][i] = num.pop(0)
        for i in range(x1, x2):
            template[i][y2] = num.pop(0)
        for i in range(y2, y1, -1):
            template[x2][i] = num.pop(0)
        for i in range(x2, x1, -1):
            template[i][y1] = num.pop(0)
    return answer
  
  
  
# 3rd try
# deque를 이용한 rotate 사용, 그 외에는 2nd try와 동일하다
# deque를 사용하기 위한 import 잊지말자!
# deque는 pop(index)를 못쓴다. 가장 왼쪽것을 빼려면 deque.popleft()를 하자
# deque.rotate(숫자)로 회전시킬 수 있다!
from collections import deque

def solution(rows, columns, queries):
    #create template
    template = [[columns*i + j + 1 for j in range(columns)] for i in range(rows)]
    
    #proceed queries
    answer = []
    for query in queries:
        #position setting
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        #saving num with deque
        num = deque()
        for i in range(y1, y2):
            num.append(template[x1][i])
        for i in range(x1, x2):
            num.append(template[i][y2])
        for i in range(y2, y1, -1):
            num.append(template[x2][i])
        for i in range(x2, x1, -1):
            num.append(template[i][y1])
        #saving min num
        answer.append(min(num))
        #rotate num
        num.rotate(1)
        #new num append
        for i in range(y1, y2):
            template[x1][i] = num.popleft()
        for i in range(x1, x2):
            template[i][y2] = num.popleft()
        for i in range(y2, y1, -1):
            template[x2][i] = num.popleft()
        for i in range(x2, x1, -1):
            template[i][y1] = num.popleft()
    return answer
