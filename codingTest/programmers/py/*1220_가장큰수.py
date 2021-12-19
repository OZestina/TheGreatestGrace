# https://programmers.co.kr/learn/courses/30/lessons/42746

#str정렬로 시도
#3,30,34의 경우 34330의 순서가 돼야 가장 큰 수를 만들 수 있는데, 이 정렬은 어떻게 한담? (지금은 33034 순)
def solution(numbers):
    num_str = [str(x) for x in numbers]
    num_str.sort()
    num_str.reverse()
    return "".join(num_str)
