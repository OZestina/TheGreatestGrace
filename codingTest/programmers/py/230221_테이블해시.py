# https://school.programmers.co.kr/learn/courses/30/lessons/147354

# 1st try
from functools import reduce

def solution(data, col, row_begin, row_end):
    #정렬
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    #나머지 계산
    mod = [0] * (row_end - row_begin + 1)
    for i in range(row_begin, row_end + 1):
        for d in data[i - 1]:
            mod[i - row_begin] += d % i
    #XOR
    answer = reduce(lambda x, y: x ^ y, mod)
    
    return answer
  
  
# 2nd try (다른 사람 풀이 참고)
# for문 돌면서 바로 xor하는게 더 빠르다
from functools import reduce

def solution(data, col, row_begin, row_end):
    answer = 0
    #정렬
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    #나머지 계산 및 xor 진행
    mod = [0] * (row_end - row_begin + 1)
    for i in range(row_begin, row_end + 1):
        for d in data[i - 1]:
            mod[i - row_begin] += d % i
        answer = answer ^ mod[i - row_begin]
    
    return answer
