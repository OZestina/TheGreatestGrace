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
