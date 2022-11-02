# https://school.programmers.co.kr/learn/courses/30/lessons/132265

# 1st try
from collections import Counter

def solution(topping):
    chul = dict()
    len_chul = 0
    bro = Counter(topping)
    len_bro = len(bro)
    
    answer = 0
    for i in topping:
        if i not in chul:
            chul[i] = 1
            len_chul += 1
        
        if bro[i] == 1:
            len_bro -= 1
        else:
            bro[i] -= 1
            
        if len_chul == len_bro: answer += 1
    
    return answer
