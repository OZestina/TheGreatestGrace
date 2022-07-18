#https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3#

#1st try
def solution(new_id):
    answer = ''
    possibleC = 'abcdefghijklmnopqrstuvwxyz.-_0123456789'
    #1
    new_id = new_id.lower()
    #2
    for i in range(len(new_id)):
        if new_id[i] in possibleC:
            answer += new_id[i]
    #3
    while '..' in answer:
        answer = answer.replace('..','.') 
    #4
    answer = answer.strip('.')
    #5
    if answer == '':
        answer = 'a'
    #6
    if len(answer) > 15 :
        answer = answer[0:15]
    answer = answer.strip('.')
    #7
    while len(answer) < 3 :
        answer += answer[len(answer)-1]
    
    return answer
  
#2nd
#line6의 possibleC를 isalpha & isdigit 으로도 변경해서 해도 된대요 (물론 여기에 .-_ 문자는 추가!)
#정규식 공부해서 정규식으로도 짜봅시다!
