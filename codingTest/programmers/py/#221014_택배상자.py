# https://school.programmers.co.kr/learn/courses/30/lessons/131704#

# 다른 사람 풀이랑 비교하기


# 1st try
def solution(order):
    answer = 1
    origin = order[0]
    sub = [i for i in range(1, order[0])]
    
    while answer < len(order):
        if order[answer] > origin:
            if order[answer] > origin + 1:
                for i in range(origin + 1, order[answer]):
                    sub.append(i)
            origin = order[answer]
            answer += 1    
        else:
            if len(sub) > 0:
                if order[answer] == sub[len(sub) - 1]:
                    answer += 1
                    sub.pop()
                else: break
            else: break
    
    return answer
  
  
  
