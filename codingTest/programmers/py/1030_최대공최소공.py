#https://programmers.co.kr/learn/courses/30/lessons/12940?language=python3

#최대공약수를 구하는데 유클리드 호제법을 사용!
#싱기해..!!

def euclidean(n, m):
    if n > m:
        return m if n % m == 0 else euclidean(m, n%m)
    else:
        return n if m % n == 0 else euclidean(n, m%n)

def solution(n, m):
    answer = []
    #최대공약수 구하기
    eu = euclidean(n,m)
    answer.append(eu)
    #최소공배수 구하기
    answer.append(m*n/eu)
    
    return answer
