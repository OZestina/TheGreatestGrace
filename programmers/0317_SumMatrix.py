#https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3

#1st try
def solution(arr1, arr2):
    answer = arr1
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer
    
# zip과 numpy를 활용하는 방법도 있는듯 하다..!
# 배워서 활용해보자!
