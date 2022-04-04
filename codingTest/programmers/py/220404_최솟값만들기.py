# https://programmers.co.kr/learn/courses/30/lessons/12941

# 1st try => 성공
def solution(A,B):
    A.sort(reverse=True)
    B.sort()
    answer = 0
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer
  
  
# 2nd try : 다른 사람의 풀이
# zip()을 이용해 for문 없이 
def solution(A,B):
    answer = [a*b for a, b in zip(sorted(A), sorted(B, reverse=True))]
    return sum(answer)
