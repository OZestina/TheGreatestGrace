# https://school.programmers.co.kr/learn/courses/30/lessons/133502#

# 3rd try, 성공
# ingredient를 한 번만 도는 것으로 바꿈..!
def solution(ingredient):
    answer = 0
    
    making = []
    last = -1
    for i in ingredient:
        if i == 1:
            if last == 3:
                answer += 1
                if len(making) > 1: last = making.pop()
                else: last = -1
            else:
                making.append(last)
                last = 1
        elif i == 2:
            if last == 1: last = 2
            else:
                making = []
                last = -1
        else:
            if last == 2: last = 3
            else:
                making = []
                last = -1
    
    return answer


# 다른 사람의 풀이
# 생각하지 못한 
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        if i == 1:
            if s[-3:] == [1, 2, 3]:
                cnt += 1
                for i in range(3):
                    s.pop()
            else: s.append(i)
        else: s.append(i)
        
    return cnt
  
# ===========================================================================

# 1st try (시간초과 실패)
def solution(ingredient):
    answer = 0
    
    i = 0
    lastbread = []
    while i < len(ingredient) - 3:
        if ingredient[i] == 1:
            if ingredient[i:i+4] == [1,2,3,1]:
                ingredient = ingredient[:i] + ingredient[i+4:]
                answer += 1
                if len(lastbread) > 0: i = lastbread.pop()
                i -= 1
            else:
                lastbread.append(i)
        i += 1

    return answer
  
  
# 2nd try (시간초과 실패)
# 심지어 1st 보다 느리다ㅎ
def check_ham(ingredient, start, end):
    burger = [2,3]
    checking = []
    idx = []
    for i in range(start + 1, end):
        if ingredient[i] != 0:
            checking.append(ingredient[i])
            idx.append(i)
    if burger == checking:
        ingredient[start] = ingredient[end] = ingredient[idx[0]] = ingredient[idx[1]] = 0
        return 1
    else: return 0
        

def solution(ingredient):
    answer = 0
    bread = []
    for i in range(len(ingredient)):
        if ingredient[i] == 1:
            bread.append(i)   
    b = 1
    while b < len(bread):
        if bread[b] - bread[b-1] >= 3:
            if check_ham(ingredient, bread[b-1], bread[b]):
                bread.remove(bread[b-1])
                bread.remove(bread[b-1])
                answer += 1
                b -= 2
        b += 1
    
    return answer
