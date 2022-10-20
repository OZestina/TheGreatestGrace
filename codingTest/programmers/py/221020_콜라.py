# https://school.programmers.co.kr/learn/courses/30/lessons/132267

# 1st try
def solution(a, b, n):
    answer = 0
    
    while n >= a:
        new_bottles = n // a * b
        answer += new_bottles
        n = n - n // a * a + new_bottles
    
    return answer
