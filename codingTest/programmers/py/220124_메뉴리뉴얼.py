# https://programmers.co.kr/learn/courses/30/lessons/72411


# 1st try
# 푸는데 시간 너무 오래 걸렸다. 성공은 함..
from itertools import combinations

def solution(orders, course):
    answer = []
    for num in course:
        answer += frequent(orders, num)
    return sorted(answer)

def frequent(orders, num):
    result = dict()
    answer = []
    for order in orders:
        if len(order) < num: continue
        for combination in combinations(sorted(order), num):
            if combination in result: result[combination] += 1
            else: result[combination] = 1
    if len(result) > 0 and max(result.values()) > 1:
        for item in [k for k,v in result.items() if max(result.values()) == v]:
            course = ""
            for a in item:
                course += a
            answer.append(course)
    return answer
  
  
# 다른 사람의 풀이
# 간결하다. 멋지다.
# 계산 시간 거의 20~30배 절감
from collections import Counter
from itertools import combinations

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)
        most_ordered = Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
    return [ ''.join(v) for v in sorted(result) ]
