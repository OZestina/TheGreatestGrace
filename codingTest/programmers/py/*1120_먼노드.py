#https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3

#1st try :  failed (2/9 통과)
def solution(n, edges):
    finish = set()
    queue = set()
    toDelete = []
    for edge in edges:
        if 1 in edge:
            queue.add(edge[1]) if edge[0] == 1 else queue.add(edge[0])
            toDelete.append(edge)
            if len(edges) == 0:
                return len(queue)

    for edge in toDelete:
        edges.remove(edge)

    finish.add(1)

    while len(edges) > 0:
        tempQ = queue.copy()
        for i in queue:
            finish.add(i)
        queue.clear()
        print('1', queue)
        for node in tempQ:
            toDelete = []
            for edge in edges:
                if node in edge:
                    toDelete.append(edge)
                    if edge[0] == node:
                        if edge[1] in finish: continue
                        queue.add(edge[1])
                    else:
                        if edge[0] in finish: continue
                        queue.add(edge[0])
            for edge in toDelete:
                edges.remove(edge)
            print('2', queue)
    return len(queue)

#2nd try
#코드 수정해서 재시도: failed (6/9 패스, 나머지 시간초과로 실패)
#방법은 맞는데 연산을 획기적으로 줄일 새로운 코드가 필요한듯하다. 복잡도를 계산해보고 어디에서 줄일 수 있는 지 확인해보자

def solution(n, edges):
    finish = set()  #검사 끝난 애들(숫자)
    queue = set()   #검사 할 애들(숫자)
    toDelete = []   #턴 끝나고 edges에서 지울 edge
    
    for edge in edges:
        if 1 in edge:
            queue.add(edge[1]) if edge[0] == 1 else queue.add(edge[0])
            toDelete.append(edge)
            if len(queue) == 0:
                return 0
            if len(edges) == 0:
                return len(queue)

    for edge in toDelete:
        edges.remove(edge)  #시작점인 1을 가진 edge들을 edges에서 지움

    finish.add(1)           #탐색이 끝난 1을 finish에 추가

    while len(edges) > 0:
        tempQ = queue.copy()
        for i in queue: finish.add(i)   #이번 턴에서 검사할 아이들 finish에 저장
        queue.clear()
        toDelete = []
        for node in tempQ:
            for edge in edges:
                if node in edge:    #검사하는 node가 edge에 있으면
                    if edge not in toDelete: toDelete.append(edge)
                    if edge[0] == node:
                        if edge[1] in finish: continue
                        queue.add(edge[1])  #다음 검사할 숫자 queue에 추가
                    else:
                        if edge[0] in finish: continue
                        queue.add(edge[0])
        for edge in toDelete:
            edges.remove(edge)
        if len(queue) == 0:
                return len(tempQ)
    return len(queue)
