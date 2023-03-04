# https://school.programmers.co.kr/learn/courses/30/lessons/161989?language=python3

# 1st try
# 통과는 하지만 리스트 pop때문인지 오래걸린다
def solution(n, m, section):
    answer = 0
    
    while section:
        start = section[0]
        end = start + m
        while section:
            if section[0] < end:
                section.pop(0)
            else:
                break
        answer += 1
        
    return answer
  
# 2nd try
# 인덱스를 넘기는 방식. 빨라졌다
def solution(n, m, section):
    answer = 0
    
    i = 0
    l = len(section)
    while (i < l):
        end = section[i] + m
        while (i < l and section[i] < end):
            i += 1
        answer += 1
    
    return answer
  
  
# 3rd try (다른 사람 풀이 참고)
# for문 한 번으로 하는 방법이 있었넹!
def solution(n, m, section):
    answer = 1
    
    before = section[0] + m
    for s in section:
        if before <= s:
            answer += 1
            before = s + m
    
    return answer
