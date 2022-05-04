#https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3

#첫번재로 짠 코드
#엄청 잘짰다고 생각했는데, 문자열 'p', 'y'를 제대로 표기 안해서 fail (다른 것도 틀린 게 있지만 일단 그거 먼저 발견)

def solution(s):
    word = s.lower()
    p = 0
    y = 0
    
    for i in word:
        if i == p:
            p = p+1
        elif i == y:
            y = y+1
        else:
            continue
    if p == y:
        answer = 'true'
    else:
        answer = 'false'
        # 여기에 print(p,y) 넣어서 제대로 counting 되는지 확인해봄!
    
    return answer
    
#수정하고 나서도 값이 안나와! 오또케!!!
#true/false 값을 반환하라고 해서 낚였는데, 스트링('')이나 그냥 true/false가 아닌 True/False (첫글자 대문자)로 써야함니다ㅎㅎ

def solution(s):
    word = s.lower()
    p = 0
    y = 0
    
    for i in word:
        if i == 'p':
            p = p+1
        elif i == 'y':
            y = y+1
        else:
            continue
    if p == y:
        answer = True
    else:
        answer = False
        
    return answer
    
#그러고 나서 다른 사람의 어-썸한 풀이를 보고야 말았던 것이었던 거시다...!!!!
#코드 줄 수도 간결하고, 풀이 시간도 (조금) 줄어듦!

def solution(s):
    return s.lower().count('p') == s.lower().count('y')
    #count() 메소드는 몰랐다고 쳐도
    #return에 바로 T/F를 리턴하는 것(이거 뭐라고 해야하지?)을 넣어둔게 굉장히 멋짐!
    #나도 잘 기억했다가 써먹어야징 :3
    
