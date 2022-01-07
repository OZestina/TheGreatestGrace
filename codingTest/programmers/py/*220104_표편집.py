# https://programmers.co.kr/learn/courses/30/lessons/81303


# 1st try
# 보여지는 내용(content)과 삭제된 순서를 저장하는 배열(delete) 및 현재 커서 위치(idx)를 저장해서 구현
# 효율성 테스트에서 절반만 통과. 더 획기적으로 줄여야 한다
def solution(n, k, cmd):
    content = [0] * n   #행 삭제 여부
    idx = k             #커서 위치
    delete = []         #행 삭제 순서
    
    for c in cmd:       #cmd 순차 실행
        #down
        if c.startswith("D"):
            step = int(c[2:])
            addition = -1
            while addition != 0:
                addition = sum(content[idx+1:idx+step+1])
                idx += step
                step = addition
        #delete
        elif c == "C":
            content[idx] = 1
            delete.append(idx)
            #삭제 후 idx 설정
            for i in range(idx+1,n):
                    if content[i] == 0:
                        idx = i
                        break
            else:
                for i in range(idx-1, -1, -1):
                    if content[i] == 0:
                        idx = i
                        break
        #up
        elif c.startswith("U"):
            step = int(c[2:])
            addition = -1
            while addition != 0:
                addition = sum(content[idx-step:idx])
                idx -= step
                step = addition
        #recover ("Z"인 경우)
        else: content[delete.pop()] = 0
        
    answer = ''
    for msg in content:
        if msg == 0: answer += 'O'
        else: answer += 'X'
    return answer
  
  
  
# 2nd try
# 데이터를 제거&복원하는 것을 실제로 진행하도록 구현
# 코드는 간결해졌으나 효율성은 0% 성공: insert가 시간을 많이 잡아먹나?
def solution(n, k, cmd):
    content = [ i for i in range(n)]    #행 삭제 여부
    idx = k                             #커서 위치
    delete = []                         #행 삭제 순서
    
    for c in cmd:       #cmd 순차 실행
        # print(f'{idx},{content}')
        #down
        if c.startswith("D"):
            step = int(c[2:])
            idx += step
        #delete
        elif c == "C":
            delete.append([content[idx],idx])
            content.remove(content[idx])
            idx = idx-1 if idx >= len(content) else idx
        #up
        elif c.startswith("U"):
            step = int(c[2:])
            idx -= step
        #recover ("Z"인 경우)
        else:
            [v,index] = delete.pop()
            content.insert(index,v)   # content.append(v) & content.sort() 도 시간 비슷
            idx = idx + 1 if index <= idx else idx
    
    answer = ''
    for i in range(n):
        if i in content: answer += 'O'
        else: answer += 'X'
    return answer
  
  
  
# 3rd try
# 메모리를 더 쓰고 연산은 줄이는 방법으로 진행 (이전 데이터를 저장해서 그대로 원복)
# 2nd try와 비슷한 정확도, 이것도 효율성은 0%
def solution(n, k, cmd):
    content = [i for i in range(n)] #행 삭제 여부
    idx = k                         #커서 위치
    delete = []                     #이전 데이터
    
    for c in cmd:       #cmd 순차 실행
        #down
        if c.startswith("D"):
            step = int(c[2:])
            idx += step
        #up
        elif c.startswith("U"):
            step = int(c[2:])
            idx -= step
        #delete
        elif c == "C":
            delete.append(content.copy())
            content.remove(content[idx])
            idx = idx-1 if idx >= len(content) else idx
        #recover ("Z"인 경우)
        else:
            a = content[idx]
            content = delete.pop()
            idx = idx + 1 if content[idx] != a else idx
    
    answer = ''
    for i in range(n):
        if i in content: answer += 'O'
        else: answer += 'X'
    return answer
