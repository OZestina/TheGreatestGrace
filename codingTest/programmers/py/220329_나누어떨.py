# https://programmers.co.kr/learn/courses/30/lessons/12910#

# 1st try => 성공
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0: answer.append(i)
    
    if len(answer) > 0: answer.sort()
    else: answer.append(-1)
    
    return answer
  
  
# 2nd try => 다른 사람의 풀이를 보고 한 줄 코딩
# return A or B : A가 참일 경우 A 리턴, A가 거짓이면 B 리턴
# 빈 리스트([])는 False로 인식하기 때문에 빈 리스트일 경우 [-1]이 리턴됨! 멋져!
def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]
