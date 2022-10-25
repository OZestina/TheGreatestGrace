# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# python class를 이용한 풀이도 있으니 찬찬히 봐보자 (다른 사람의 풀이)



# 1st try
def solution(fees, records):
    parking = dict()
    temp = dict()
    
    for record in records:
        time = int(record[:2]) * 60 + int(record[3:5])
        car = record[6:10]
        if car in temp:
            if car in parking:
                parking[car] += time - temp[car]
            else:
                parking[car] = time - temp[car]
            temp.pop(car)
        else:
            temp[car] = time
    
    time = 23 * 60 + 59
    for car in temp:
        if car in parking:
            parking[car] += time - temp[car]
        else:
            parking[car] = time - temp[car]
        
    answer = []
    for car in sorted(parking):
        time = parking[car] - fees[0] if parking[car] - fees[0] >= 0 else 0
        amount = time // fees[2] if time // fees[2] == time / fees[2] else time // fees[2] + 1
        answer.append(fees[1] + amount * fees[3])
    return answer
