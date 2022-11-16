# https://school.programmers.co.kr/learn/courses/30/lessons/131701


# 1st try
def solution(elements):
    l = len(elements)
    answer = set(elements)
    answer.add(sum(elements))
    
    for i in range(2, l):
        temp = sum(elements[:i])
        answer.add(temp)
        for j in range(len(elements)):
            temp = temp - elements[j] + elements[(j+i) % l]
            answer.add(temp)
        
    return len(answer)
  
  
# 2nd try (다른 사람의 풀이)
# add라는 len()만큼의 배열을 만들어서 뒷 수를 계속 더해주는 
def solution(elements):
    answer = set()
    l = len(elements)

    add = [0 for i in range(l)]
    for i in range(l):
        add = [add[j] + elements[(i+j) % l] for j in range(l)]
        
        for a in add:
            answer.add(a)

    return len(answer)
