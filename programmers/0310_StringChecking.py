#https://programmers.co.kr/learn/courses/30/lessons/12918

#1st try
def solution(s):
    a = ["0","1","2","3","4","5","6","7","8","9"]
    b = 0
    if len(s) == 4 or len(s) == 6:
        for i in list(s):
            if i in a:
                b += 1
            else:
                continue
            if b == len(s):
                answer = True
            else:
                answer = False
    else:
        answer = False
    
    return answer


#2nd try with newly learned .isdigit()! (and .isalpha())
def solution(s):
    if len(s) == 4 or len(s) == 6:
        answer = s.isdigit()
    else:
        answer = False
        
    return answer

#3rd way with [Try/Except] --> 이게 처음에 하려고 했던건데 try/except가 어떻게 검색해야 하는지 조차 기억 안나서 못함ㅎㅎ
def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            answer = True
        except:
            answer = False
    else:
        answer = False
    
    return answer
