# https://programmers.co.kr/learn/courses/30/lessons/17681#

# 1st try => 성공
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = format(arr1[i] | arr2[i], 'b').replace("1", "#").replace("0"," ")
        while len(a) < n:
            a = " "+a
        answer.append(a)
    return answer
  

# 2nd try => 다른 사람의 풀이 참고
# rjust 함수를 배웠다! (오른쪽 정렬하고 빈 칸 채울 수 있음)
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = format(arr1[i] | arr2[i], 'b').rjust(n,'0').replace("1", "#").replace("0"," ")
        answer.append(a)
    return answer
