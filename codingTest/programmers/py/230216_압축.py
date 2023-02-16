# https://school.programmers.co.kr/learn/courses/30/lessons/17684

# 1st try
def solution(msg):
    answer = []
    
    dictionary = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    
    s_i = 0
    word_i = 27
    while s_i < len(msg):
        temp = 0
        for e_i in range(s_i + 1, len(msg) + 1):
            try:
                temp = dictionary[msg[s_i : e_i]]
                if e_i == len(msg):
                    answer.append(temp)
                    s_i = e_i
                    break
            except:
                answer.append(temp)
                dictionary[msg[s_i : e_i]], word_i = word_i, word_i + 1
                s_i = e_i - 1
                break
    
    return answer
  
  
# 2nd try (다른 사람의 풀이)
# msg에서 남은 부분만 다시 할당해주면서 진행
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    word_i = 27
    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]], word_i = word_i, word_i + 1
                msg = msg[i-1:]
                break

    return answer
