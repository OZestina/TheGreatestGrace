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

#꺆 새벽에 코딩요정 소환해서 해결함!
#꾸르팁: 테스트케이스 추가 (기본적인 0, 1 부터 확인해보자^^..)

def solution(n):
    a = 0
    #요기에서 a == 1 인 경우, 1 < 1로 인식하여 a가 0으로 진행되는 상황 발생! 삐뽀삐뽀
    #작거나 같은걸로 바꽈줬습니당!
    while 3 ** a <= n:
        a = a + 1
    
    n3_list = [0 for i in range(a)]
    x = n
    
    while a > 0:
        if x >= 2*3**(a-1):
            n3_list[a-1] = 2
            x = x - 2 * 3 ** (a-1)            
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

#다른 사람 풀이 보기 두렵다^^...
#투비컨티뉴
