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
