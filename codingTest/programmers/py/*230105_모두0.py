# 

# 1st try => 시간초과 실패
# 노드를 계산해서 끝 노드들부터 계산하는 방식. sorted()로 시간 단축을 도모했지만 결국은 시간초과
from collections import defaultdict

def solution(a, edges):
    # 0으로 만들 수 없는 경우
    if sum(a) != 0:
        return -1
    
    # 0으로 만드는 수 계산
    answer = 0
    connection = defaultdict(list)
    for e1, e2 in edges:
        connection[e1] += [e2]
        connection[e2] += [e1]
    
    while len(connection) > 1:
        arr = sorted(connection, key=lambda x: len(connection[x]))
        for c in arr:
            if len(connection[c]) == 1:
                temp = a[c]
                answer += abs(temp)
                a[connection[c][0]] += temp
                connection[connection[c][0]].remove(c)
                connection.pop(c)
            else:
                break
    
    return answer
