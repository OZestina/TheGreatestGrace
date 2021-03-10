#https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

#1st try -> nice one! (yayy)
def solution(answers):
    answer = []
    score = [0,0,0]

    stu1_5 = [1,2,3,4,5]
    stu2_8 = [2,1,2,3,2,4,2,5]
    stu3_10 = [3,3,1,1,2,2,4,4,5,5]
        
    for i in range(len(answers)):
        if stu1_5[i%5] == answers[i]: #5가 어디서 나왔죠? len(stu1_5)에서 나왔져...
            score[0] = score[0]+1
        if stu2_8[i%8] == answers[i]:
            score[1] = score[1]+1
        if stu3_10[i%10] == answers[i]:
            score[2] = score[2]+1
    
    a = max(ans)
    if a == score[0]:
        answer.append(1)
    if a == score[1]:
        answer.append(2)
    if a == score[2]:
        answer.append(3)
    
    return answer
  
#2nd try with enumerate 함수 (새로 앎)
def solution(answers):
    answer = []
    score = [0,0,0]

    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i,v in enumerate(answers):
        if v == s1[i%len(s1)]:
            score[0] += 1
        if v == s2[i%len(s2)]:
            score[1] += 1
        if v == s3[i%len(s3)]:
            score[2] += 1
            
    for i,v in enumerate(score):
        if v == max(score):
            answer.append(i+1)
    
    return answer
  
#3rd (other ppl's code)
def solution(answers):
    p = [[1,2,3,4,5], 
         [2,1,2,3,2,4,2,5], 
         [3,3,1,1,2,2,4,4,5,5]]
    s = [0] * len(p)
    answer = []
    
    for i,v in enumerate(answers):
        for ind,val in enumerate(p):
            if v == val[i%len(p[ind])]: #if v == val[i%len(val)]:
                s[ind] += 1
    
    for i,v in enumerate(s):
        if v == max(s):
            answer.append(i+1)
    
    return answer
