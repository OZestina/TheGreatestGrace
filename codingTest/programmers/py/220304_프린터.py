# https://programmers.co.kr/learn/courses/30/lessons/42587

# 1st try
# 정답이고 걸린 시간도 적은데 뭔가 맘에 안든다.
def solution(priorities, location):
    answer = 0
    position = 0
    mydoc = priorities[location]
    
    doc = {}          #내 문서보다 높은 우선순위 문서의 위치 기록용
    sameprior = []    #내 문서와 같은 문서의 위치 기록용
    for i in range(len(priorities)):
        if priorities[i] < mydoc:           #우선순위 낮은 애는 countinue
            continue
        elif priorities[i] > mydoc:         #우선순위 높
            if priorities[i] in doc:
                doc[priorities[i]] += [i]
            else:
                doc[priorities[i]] = [i]
        else:                               # priorities[i] == mydoc
            sameprior += [i]
    
    for k,v in sorted(doc.items(), reverse=True): #doc에 있는 모든 문서를 대상으로 answer와 마지막 출력 position계산
        answer += len(v)
        if position == 0:
            position = v[-1]
        else:
            if v[0] > position: position = v[-1]
            else:
                temp = v[0]
                for i in v:
                    if i < position:
                        temp = i
                    else:
                        break
                position = temp
        
    if position <= location:                      #우선순위 동일한 파일에 대해 answer 계산
        for i in sameprior:
            if i >= position and i <= location:
                answer += 1
    else:   # position > location
        for i in sameprior:
            if i <= location or i > position:
                answer += 1

    return answer
  
  
  
# 2nd try (다른 사람 풀이 참조)
# (편안)
# 하지만 정말 극한의 시간절약을 추구해야 한다면 (메모리를 굉장히 많이 쓰면서라도) 1st try도 나쁘지 않아보인다
def solution(priorities, location):
    answer = 0
    pos = 0
    doc = len(priorities) - 1
    
    while True:
        if max(priorities) == priorities[pos]:
            priorities[pos] = 0
            answer += 1
            if location == pos:
                break
        pos = pos+1 if pos < doc else 0
        
    return answer
