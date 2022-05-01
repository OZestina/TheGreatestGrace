# https://programmers.co.kr/learn/courses/30/lessons/12949

# 1st try => 성공
def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        result = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                temp += arr1[i][k] * arr2[k][j]
            result.append(temp)
        # print(result)
        answer.append(result)
    
    return answer


# 2nd try: 다른 사람의 풀이
# 기억해둡시다 zip(*[2차배열]) => (행,행,행) -> (열,열,열)
def solution(arr1, arr2):
    answer = []
    for arr1_row in arr1:
        for arr2_col in zip(*arr2):
            answer.append(sum(a*b for a,b in zip(arr1_row, arr2_col)))
    return answer

# 2-1) 한 줄로 한다면?
def solution(arr1, arr2):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*arr2)] for row in arr1]
