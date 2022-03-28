# https://programmers.co.kr/learn/courses/30/lessons/12943

# 1st try
def solution(num):
    answer = 0
    for i in range(500):
        if num == 1: return answer
        
        if num % 2: num = num*3 + 1
        else: num /= 2
        
        answer += 1  
        
    return -1
  
# if문을 삼항 연산자로 쓰면 더 빠르다..!
def solution(num):
    answer = 0
    for i in range(500):
        if num == 1: return answer
    
        num = num*3 + 1 if num % 2 == 1 else num//2
        answer += 1
    
    return -1
