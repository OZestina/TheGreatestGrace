# https://school.programmers.co.kr/learn/courses/30/lessons/86971?language=python3

# 코드는 더러운 것 같으나... 속도는 빨라서 괜찮나 싶다
def solution(n, wires):
    answer = -1
    #각 노드에 연결된 노드들 체크
    connection = dict()
    for wire in wires:
        if wire[0] not in connection:
            connection[wire[0]] = [wire[1]]
        elif wire[0] in connection:
            connection[wire[0]].append(wire[1])
        if wire[1] not in connection:
            connection[wire[1]] = [wire[0]]
        elif wire[1] in connection:
            connection[wire[1]].append(wire[0])
    #맨 마지막 노드인 것 정리
    leaf = []
    for i in connection:
        if len(connection[i]) == 1:
            leaf.append(i)
    #
    for wire in wires:
        if wire[0] not in leaf and wire[1] not in leaf:
            checked = {wire[0]}
            queue = connection[wire[0]].copy()
            queue.remove(wire[1])
            while len(queue) > 0:
                temp = queue.pop(0)
                checked.add(temp)
                for i in connection[temp]:
                    if i not in checked:
                        queue.append(i)
            diff = 2*len(checked)-n if 2*len(checked)-n > 0 else n-2*len(checked)
            if answer == -1:
                answer = diff
            else:
                answer = diff if diff < answer else answer
    if answer == -1:
        answer = n - 2
    return answer
  
  
  
  
# 다른 사람의 풀이
# 이중for문을 한 줄로 쓰는거 신기..! (참고: https://somjang.tistory.com/entry/Python-%EC%9D%B4%EC%A4%91-for-%EB%AC%B8-%ED%95%9C-%EC%A4%84%EB%A1%9C-%EC%9E%91%EC%84%B1%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)
def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        #연결 노드를 모두 정리해주기 위해 n*n번 돌려준거였다
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        ans = min(ans, abs(2 * len(s) - n))
    return ans
  
