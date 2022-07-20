#https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3

#1st try => 성공
#int를 str으로 변환 후 내림차순 정렬, 그 후 다시 int로 변환!
def solution(n):
    a = ''.join(sorted(str(n),reverse=True))
    answer = int(a)
    return answer
