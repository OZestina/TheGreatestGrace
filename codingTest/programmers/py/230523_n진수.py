# https://school.programmers.co.kr/learn/courses/30/lessons/17687

# 1st try
def get_num(n, num):
    base = '0123456789ABCDEF'
    if num < n:
        return base[num]
    return get_num(n, num//n) + base[num%n]

def solution(n, t, m, p):
    answer = ''
    
    num = '0'
    number = 1
    while len(num) < t * m:
        num += get_num(n, number)
        number += 1
    
    for i in range(t):
        answer += num[i*m + p - 1]
        
    return answer
