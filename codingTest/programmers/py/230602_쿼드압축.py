# https://school.programmers.co.kr/learn/courses/30/lessons/68936#

# 1st try
def count_0_1(arr):
    answer = [0, 0]
    length = len(arr)
    
    for i in range(length):
        for j in range(length):
            if arr[i][j] == 0:
                answer[0] += 1
            elif arr[i][j] == 1:
                answer[1] += 1
    return answer


def solution(arr):
    length = len(arr)
    
    # len(arr) < 4 일 경우 별도 처리
    if length == 1:
        return count_0_1(arr)
    if length == 2:
        if arr[0][0] == arr[0][1] == arr[1][0] == arr[1][1]:
            answer = [0,0]
            answer[arr[0][0]] = 1
            return answer
        return count_0_1(arr)
    
    
    # 최초 압축 진행
    rounds = length // 2
    s = length // rounds
    for i in range(rounds):
        for j in range(rounds):
            if arr[i*s][j*s] == arr[i*s+1][j*s] == arr[i*s][j*s+1] == arr[i*s+1][j*s+1]:
                arr[i*s+1][j*s] = arr[i*s][j*s+1] = arr[i*s+1][j*s+1] = 3

    
    # 작은 사각형부터 만들어서 큰 사각형으로 합치는 방식
    while rounds > 1:
        rounds //= 2
        s = length // rounds
        
        for i in range(rounds):
            for j in range(rounds):
                if arr[i*s][j*s] == arr[i*s+s//2][j*s] == arr[i*s][j*s+s//2] == arr[i*s+s//2][j*s+s//2] and arr[i*s+s//4][j*s+s//4] == arr[i*s+s//2+s//4][j*s+s//4] == arr[i*s+s//4][j*s+s//2+s//4] == arr[i*s+s//2+s//4][j*s+s//2+s//4] == 3:
                    arr[i*s+s//2][j*s] = arr[i*s][j*s+s//2] = arr[i*s+s//2][j*s+s//2] = 3
        
    
    return count_0_1(arr) # 0, 1 count
    

    
# 다른 사람의 풀이
# 재귀를 이용해 큰 사각형부터 확인, 숫자가 다를 경우 작은 사각형을 검사하는 방식
# 코드도 간결하고 연산도 적다

def solution(arr):
    answer = [0, 0]

    def check(size, x, y):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1
    check(len(arr),0,0)


    return answer
