# https://programmers.co.kr/learn/courses/30/lessons/43236?language=python3#

#1st try with Fairy
#조합을 활용해 모든 경우의 수를 구해보자
#테스트 통과, 제출 실패 (시간초과) => 다른 방법을 생각해보자
from itertools import combinations

def solution(distance, rocks, n):
    # 돌을 모두 없앨 경우
    if n == len(rocks): return distance

    # 리턴할 최소거리 저장용 변수
    answer = -1

    # 가능한 남은 돌 경우의 수 찾기
    for combination in combinations(sorted(rocks), len(rocks) - n):
        small = combination[0]
        combination = list(combination) + [distance]
        prev_rock = 0
        for rock in combination:
            dif = rock - prev_rock
            small = dif if dif < small else small
            prev_rock = rock
            
        answer = small if small > answer else answer
    return answer
