# 

# 1st try (실패)
# 중간에 바꾸지 않아도 되는 블럭이 길어서 온 길을 다시 되돌아가는게 나을 경우 최소 거리를 계산하지 못함
def up_down(c):     # 'A'에서 char c까지의 최소 조작 수 리턴
    if c == 'N':  return 13
    elif c < 'N': return ord(c) - ord('A')
    else:         return ord('Z') - ord(c) + 1

def solution(name):
    length = len(name)
    #changed에 'A'가 아니어서 바꿔야하는 자리 저장
    changed = []
    for i in range(length):
        if name[i] == 'A': changed.append(1)
        else:              changed.append(0)
    #초기값 세팅 (첫자리 글자 변경 후 다음 자리로 넘어감)
    answer = up_down(name[0])
    changed[0] = 1
    #다음자리로 이동하는 과정
    current = 0
    while 0 in changed:
        # (현재 자리 기준) 오른쪽으로 가장 가까운 0 찾기
        to_right = (current + 1) % length
        step_to_right = 1
        while changed[to_right] == 1:
            step_to_right += 1
            to_right = (to_right + 1) % length
        # (현재 자리 기준) 왼쪽으로 가장 가까운 0 찾기
        to_left = (length + current - 1) % length
        step_to_left = 1
        while changed[to_left] == 1:
            step_to_left += 1
            to_left = (length + to_left - 1) % length
        # to_right, to_left 중 가장 가까운 0으로 current 변경, 이동거리만큼 answer 증가
        if step_to_right <= step_to_left:
            current = to_right
            answer += step_to_right
        else:
            current = to_left
            answer += step_to_left
        # current에 있는 글자 변경, 조작 수 만큼 answer 증가
        changed[current] = 1
        answer += up_down(name[current])
        
    return answer
  
  
# 2nd try (성공)
# 접근 방법을 바꿔서, 가장 큰 A 블록을 구해서 우회하는 최단 거리를 계산해봄
def up_down(c):     # 'A'에서 char c까지의 최소 조작 수 리턴
    if c == 'A':  return 0
    elif c == 'N':return 13
    elif c < 'N': return ord(c) - ord('A')
    else:         return ord('Z') - ord(c) + 1

def solution(name):
    length = len(name)
    
    #첫 글자가 'A'인 경우 이를 포함하는 'A' 블록 찾기
    include_first = [1, 0]
    if name[0] == 'A':
        for s in range(-1, -length, -1):
            if name[s] != 'A':
                include_first[0] = s + 1
                break
        else:   #if all charactor is 'A'
            return 0
        for e in range(1, length):
            if name[e] != 'A':
                include_first[1] = e
                break
    # 두 번째 글자 이후의 가장 긴 'A' 블록 찾기
    big_A = [0, 0]
    temp_start = 0
    for i in range(1, length):
        if name[i] == 'A' and temp_start == 0: temp_start = i
        elif name[i] != 'A' and temp_start != 0: 
            if big_A[1] - big_A[0] < i - temp_start: big_A = [temp_start, i]
            temp_start = 0
    if temp_start != 0:
        if big_A[1] - big_A[0] < i + 1 - temp_start: big_A = [temp_start, i + 1]
            
    answer = length - 1
    #최소이동 조작 개수 계산
    #   1) big_A를 지나지 않는 가장 효율적인 조작 개수
    if big_A[0] != 0:
        temp = length - (big_A[1] - big_A[0]) - 1 + min([big_A[0] - 1, length - big_A[1]])
        if temp < answer: answer = temp
    #   2) include_first 효율적으로 피하기
    if include_first[0] != 1:
        temp = length + include_first[0] - include_first[1] - 1 + min([abs(include_first[0]) + 1, include_first[1]])
        if temp < answer: answer = temp
    
    #문자 조작 개수 계산
    for i in range(length):
        answer += up_down(name[i])
        
    return answer
  
  
# 3rd try (다른 사람의 풀이 참고)
# 이것이 출제자의 취지였던것같다 (greedy)
# (A로 시작하는 문자열의 경우 어떻게 하지 하다가 아예 분리해서 풀었는데, 이 방법을 보니 이렇게도 할 수 있구나 싶다ㅎㅎ)
def solution(name):
    answer = 0
    #모든 문자 변경 조작 카운트
    num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
    for ch in name:
        answer += num_char[ord(ch) - ord('A')]

    n = len(name)
    move = n - 1
    idx = 0
    while idx < n:
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)
        idx = next_idx
    answer += move
    return answer
