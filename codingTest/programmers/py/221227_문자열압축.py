# https://school.programmers.co.kr/learn/courses/30/lessons/60057#

# 1st try
def root(flag):   #aaaaaaaaaa의 경우 10a여서 한 자리수 더해줘야 하니 flag 계산 고고
    while flag > 1:
        if flag % 10 != 0:
            return 0
        flag /= 10
    return 1

def compression(s, part, length):
    last = ""
    count = 0
    
    for i in range(0, length // part):
        if s[i*part:(i+1)*part] == last:
            if flag == 1:
                count += 1
                flag += 1
            else:
                flag += 1
                if root(flag):
                    count += 1
        else:
            last = s[i*part:(i+1)*part]
            count += part
            flag = 1
    return count + length % part

def solution(s):
    length = len(s)
    answer = length
    
    for i in range(1, length // 2 + 1):
        temp = compression(s, i, length)
        if temp < answer:
            answer = temp
    
    return answer
  
  
# 2nd try
# 매번 root(flag) 대신 마지막에 len(str(flag))를 더해주는 방식
# 근데 전반적인 속도는 1st 방법이 낫다 (아마 int->str이 오래 걸리는 듯)
def compression(s, part, length):
    last = ""
    count = 0
    flag = 1
    
    for i in range(0, length // part):
        if s[i*part:(i+1)*part] == last:
            flag += 1
        else:
            last = s[i*part:(i+1)*part]
            count += part
            if flag != 1:
                count += len(str(flag))
            flag = 1
    if flag != 1:
        count += len(str(flag))
    return count + length % part

def solution(s):
    length = len(s)
    answer = length
    
    for i in range(1, length // 2 + 1):
        temp = compression(s, i, length)
        if temp < answer:
            answer = temp
    
    return answer
  
  
  
# 3rd try (다른 사람의 풀이)
# 접근 방식은 비슷, 반복된 문자열의 수를 str으로 만드는 데 "{}".format()을 쓰니 더 빨랐다 (line 91, 92)
def solution(s):
    answer = len(s)
    for x in range(1, len(s)//2+1):
        d = 0
        comp = ''
        c = 1
        for i in range(0, len(s), x):
            temp = s[i:i+x]
            if comp == temp:
                c += 1
            elif comp != temp:
                d += len(temp)
                if c > 1:
                    #d += len(str(c))
                    d += len("{}".format(c))
                c = 1
                comp = temp
        if c > 1:
            d += len("{}".format(c))
        answer = min(answer, d)
    return answer
