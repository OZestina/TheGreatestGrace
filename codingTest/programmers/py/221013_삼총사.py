# https://school.programmers.co.kr/learn/courses/30/lessons/131705

def find3(number, sumn, start, remain):
    count = 0
    if remain == 1:
        for i in range(start, len(number) - remain + 1):
            if sumn + number[i] == 0:
                count += 1
        return count
    else:
        for i in range(start, len(number) - remain + 1):
            count += find3(number, sumn + number[i], i+1, remain - 1)
        return count

def solution(number):
    answer = find3(number, 0, 0, 3)
    
    return answer
