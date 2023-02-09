# https://school.programmers.co.kr/learn/courses/30/lessons/12987

# 1st try
# 작은 수 부터 이기는 패를 선택
def solution(A, B):
    answer = 0
    
    A = sorted(A)
    B = sorted(B)
    a, b = 0, 0
    
    while b < len(B):
        if A[a] < B[b]:
            a += 1
            b += 1
            answer += 1
        else:
            b += 1
    
    return answer
  
  
# 2nd try (다른 사람 풀이 참고)
# 굳이 변수 하나를 더 쓰면서 별도 연산하지 않고 for문으로 진행 (어짜피 B는 마지막까지 확인해야하니까)
def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    a = 0
    for b in range(len(B)):
        if A[a] < B[b]:
            answer += 1
            a += 1

    return answer
