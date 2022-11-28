# https://school.programmers.co.kr/learn/courses/30/lessons/138476

# 1st try
def solution(k, tangerine):
    level = {}
    for t in tangerine:
        if t not in level: level[t] = 1
        else: level[t] += 1
    
    answer = 0
    total = 0
    for i in sorted(level.values(), reverse=True):
        total += i
        answer += 1
        if total >= k:
            break
    return answer
  
  
  
# 2nd try (using Counter)
# collections.Counter()가 확실히 빠르다!
from collections import Counter

def solution(k, tangerine):
    level = Counter(tangerine)
    
    answer = 0
    for i in sorted(level.values(), reverse=True):
        k -= i
        answer += 1
        if k <= 0:
            break
    return answer
