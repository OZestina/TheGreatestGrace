# https://school.programmers.co.kr/learn/courses/30/lessons/42627

# 1st try
from heapq import heappush, heappop

def solution(jobs):
    l = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    
    heap = []
    current = 0
    answer = 0
    while len(jobs) or len(heap):
        #fill heap
        while len(jobs) and jobs[0][0] <= current:
            heappush(heap, [jobs[0][1], jobs[0][0]])
            jobs.pop(0)
        #pop heap
        try:
            time, wait = heappop(heap)
            answer += current - wait + time
            current += time
        except:
            current += 1
    
    return answer // l
