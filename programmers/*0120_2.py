#https://programmers.co.kr/learn/courses/30/lessons/68935
#30분만 해보고 안되면 자야지 (새벽 1:30)
#ㄴ> 1시간 30분 걸림^^ (그마저도 80% 패스, 2문제는 실패)

def solution(n):
    a = 0
    while 3**a < n:
        a = a+1
    
    n3_list = [0 for i in range(a)]
    x = n
    
    while a > 0:
        if x >= 2*3**(a-1):
            n3_list[a-1] = 2
            x = x - 2*3**(a-1)            
        elif x >= 3**(a-1):
            n3_list[a-1] = 1
            x = x - 3**(a-1)
        elif x == 0:
            break
        a=a-1    
    
    b = len(n3_list) -1
    answer = 0
    
    for i in n3_list:
        answer = answer + i * 3**b
        b -= 1
    return answer
