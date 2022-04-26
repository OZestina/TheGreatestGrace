# https://programmers.co.kr/learn/courses/30/lessons/72412#

# 1st try: 정확성 통과, 효율성 fail
# 조건에 맞는 지원자만 count하도록
def solution(info, query):
    answer = []

    new_info = [i.split() for i in info]
    new_query = [i.split() for i in query]

    for i in new_query:
        temp = set()

        for k in range(len(new_info)):
            if int(i[7]) <= int(new_info[k][4]): temp.add(k)
        count = 0
        for k in temp:
            if i[0] == '-' or i[0] == new_info[k][0]:
                if i[2] == '-' or i[2] == new_info[k][1]:
                    if i[4] == '-' or i[4] == new_info[k][2]:
                        if i[6] == '-' or i[6] == new_info[k][3]:
                            count += 1

        answer.append(count)

    return answer


# 2nd try: 정확성 통과(1st보다 살짝 나아짐), 효율성 fail
# 지원자 조건을 미리 나눠둬서 set 차집합으로 구하기
def solution(info, query):
    answer = []
    
    java = set()
    cpp = set()
    python = set()
    back = set()
    front = set()
    jun = set()
    sen = set()
    pizza = set()
    chicken = set()
    score = []
    
    for i in range(len(info)):
        new_info = info[i].split()
        
        if new_info[0] == 'java': java.add(i)
        elif new_info[0] == 'cpp': cpp.add(i)
        else: python.add(i)
        
        if new_info[1] == 'frontend': front.add(i)
        else: back.add(i)
        
        if new_info[2] == 'junior': jun.add(i)
        else: sen.add(i)
        
        if new_info[3] == 'pizza': pizza.add(i)
        else: chicken.add(i)
        
        score.append(new_info[4])
        
    for newQ in query:
        i = newQ.split()
        temp = set()
        
        for k in range(len(score)):
            if int(i[7]) <= int(score[k]): temp.add(k)
        
        if i[0] == 'java': temp = temp - cpp - python
        elif i[0] == 'cpp': temp = temp - python - java
        elif i[0] == 'python': temp = temp - cpp - java
        
        if i[2] == 'backend': temp = temp - front
        elif i[2] == 'frontend': temp = temp - back
        
        if i[4] == 'junior': temp = temp - sen
        elif i[4] == 'senior': temp = temp - jun
        
        if i[6] == 'pizza': temp = temp - chicken
        elif i[6] == 'chicken': temp = temp - pizza
        
        answer.append(len(temp))
        
    return answer

