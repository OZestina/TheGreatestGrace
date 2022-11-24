# https://school.programmers.co.kr/learn/courses/30/lessons/12913

# 1st try
def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][0:j] + land[i-1][j+1:])
    return max(land[len(land)-1])
    
    return max(land[-1]) # 맞다맞다 왜 이 생각을 못했지ㅋㅋㅋㅋㅋ
