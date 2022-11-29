# https://school.programmers.co.kr/learn/courses/30/lessons/92335

# 1st try
def isprime(n):
    if n == 1 or n == 0: return 0
    if n in [2, 3, 5, 7, 11, 13]: return 1
    if n % 2 == 0: return 0
    for i in range(3, int(n**(1/2)) + 1, 2):
        if n % i == 0: return 0
    return 1


def solution(n, k):
    num_k = ''
    while n > 0:
        num_k += str(n % k)
        n //= k
    
    temp = 0
    answer = 0
    for i in range(len(num_k)-1, -1, -1):
        if num_k[i] == '0':
            answer += isprime(temp)
            temp = 0
        else:
            temp = int(num_k[i]) + temp * 10    
    answer += isprime(temp)
    return answer
  
  
  
# 2nd try (다른 사람의 풀이 참고)
# str역순으로 뒤집기 => str[::-1]
# str.split()을 이용해 한 단위씩 
def isprime(n):
    if n == 1 or n == 0: return 0
    if n in [2, 3, 5, 7, 11, 13]: return 1
    if n % 2 == 0: return 0
    for i in range(3, int(n**(1/2)) + 1, 2):
        if n % i == 0: return 0
    return 1


def solution(n, k):
    num_k = ''
    while n > 0:
        num_k += str(n % k)
        n //= k
    
    answer = 0
    for i in num_k[::-1].split('0'):
        try:
            answer += isprime(int(i))
        except:   # 00 등이 나왔을 경우 빈칸 처리용
            continue
    return answer
