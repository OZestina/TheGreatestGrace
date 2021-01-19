#https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    m=str(n)
    
    gae = list(m)
    a = len(gae) - 1
    
    while a > -1:
        answer.append(int(gae[a]))
        a = a-1    
    
    return answer
    
    
    
#awesome한 코드 발견!

def solution(n):
    answer = [int(i) for i in str(n)][::-1]
    
    return answer
    
#이렇게 하면 어떻게 연산되는지 코딩요정에게 물어볼것! -> 물어봄! 이해됨!
#저렇게 대괄호 안에 쓰면 자동으로 리스트 만들어주는거 싱기하다...
#[처음:(부터)끝:(까지):-1(의 순서로 정렬)]

To. 코딩요정님
#모르는거 이상하게 써놔서 뭘 물어보려고 했는지 헷갈려서 다른거 설명들음ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
#궁금했던 거: 위에 코드랑 아래 코드랑 메모리 & 속도 차이가 (1)얼마나 의미있는건지 (2)어떻게 계산하는건지를 물어보려고 했었음
