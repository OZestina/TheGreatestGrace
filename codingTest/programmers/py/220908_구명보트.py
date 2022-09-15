# https://school.programmers.co.kr/learn/courses/30/lessons/42885#

# 2nd try
# 정렬 후 짝지을 수 있는 개수를 계산하는 방식
def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    
    while left < right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
        right -= 1
    return len(people) - answer
  
# ============================================================

# 1st try => 성공은 했지만 틀린 코드..! (최대 2명 인원제한이 있었다)
# 정렬 후 구명보트 짝을 맞춰서 계산하는 방식
def solution(people, limit):
    answer = 0
    #몸무게가 무거운 순으로 정렬, 앞&뒤 인덱스 생성 및 초기화
    people.sort(reverse=True)
    left = 0
    right = len(people) - 1
    #몸무게==limit인 경우 계산
    while True:
        if people[left] == limit:
            answer += 1
            left += 1
        else:
            break
    if left > right:    #모든 사람이 limit의 무게를 가지고 있을 경우
        return answer
    #앞&뒤 인덱스 이동해가며 구명보트 매칭
    while left <= right:
        available = limit - people[left]
        left += 1
        answer += 1
        if left > right:
            break
        while available > 0 and left <= right:
            if available >= people[right]:
                available -= people[right]
                right -= 1
            else:
                break
    return answer
