# https://school.programmers.co.kr/learn/courses/30/lessons/131703#

# 1st try
def solution(beginning, target):
    # 두 테이블의 차이를 differ에 저장
    differ = []
    for i in range(len(target)):
        differ.append([abs(target[i][j] - beginning[i][j]) for j in range(len(target[0]))])
    
    # 뒤집는 횟수 count에 저장
    count = 0
    for j in range(len(differ[0])):
        if differ[0][j] == 1:
            count += 1
            for i in range(len(differ)):
                differ[i][j] = 0 if differ[i][j] == 1 else 1
    for i in range(len(differ)):
        if differ[i][0] == 1:
            count += 1
            for j in range(len(differ[0])):
                differ[i][j] = 0 if differ[i][j] == 1 else 1
                
    # 최소 뒤집기 횟수 계산
    maxi = len(target) + len(target[0])
    answer = count if count < maxi - count else maxi - count
        
    # target을 만들 수 있는지 (differ을 모두 0으로 만들 수 있는지) 확인 후 리턴
    possible = sum([sum(i) for i in differ])
    if possible == 0:
        return answer
    return -1
