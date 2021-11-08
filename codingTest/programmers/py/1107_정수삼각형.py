#https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    floor = len(triangle)
    if floor == 1:
        return triangle[0][0]
    
    while floor > 1:
        for i in range(len(triangle[floor-2])):
            if triangle[floor-1][i] > triangle[floor-1][i+1]: triangle[floor-2][i] += triangle[floor-1][i]
            else: triangle[floor-2][i] += triangle[floor-1][i+1]     
        floor -= 1
    
    return triangle[0][0]
