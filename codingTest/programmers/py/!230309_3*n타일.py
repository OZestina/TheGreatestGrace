# https://school.programmers.co.kr/learn/courses/30/lessons/12902#

# 1st try
# 큰 수를 계산하기 위해서는 작은 수가 필요해, 앞에서부터 순차적으로 접근하는 방식으로 진행
def tile(n):
    if n == 1:
        return 3
    return 2

def arr_tile(n, arr):
    if arr[n] > -1:
        return arr[n]
    count = 2
    for i in range(n - 1, 0, -1):
        count = (count + tile(i) * arr_tile(n - i, arr)) % 1000000007
    arr[n] = count % 1000000007
    return arr[n]

def solution(n):
    #가로 길이가 짝수면 채우지 못하므로 0 리턴
    if n % 2: return 0
    
    #작은 input 처리
    if n == 2: return 3
    if n == 4: return 11
    if n == 6: return 41
    
    #이후 n//2 값으로 진행
    n = n // 2
    
    #이미 계산한 내용 저장용 arr생성 && 초기값 세팅
    arr = [-1] * (n + 1)
    arr[1] = 3
    arr[2] = 11
    arr[3] = 41
    
    #작은 수부터 순차적으로 계산
    for i in range(4, n + 1):
        arr[i] = arr_tile(n, arr)
    
    return arr[n]
