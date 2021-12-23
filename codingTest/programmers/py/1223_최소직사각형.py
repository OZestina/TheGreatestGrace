# https://programmers.co.kr/learn/courses/30/lessons/86491
# 1st->2nd->3rd로 갈수록 코드는 간단해져보이지만
# 걸리는 시간과 메모리를 따지면 사실 1st가 가장 낫다^^

#1st try
def solution(sizes):
    width = []
    height = []
    for size in sizes:
        if size[0] > size[1]:
            width.append(size[0])
            height.append(size[1])
        else:
            width.append(size[1])
            height.append(size[0])
    w = max(width)
    h = max(height)
    return w*h

#2nd try
# if~else문 없애기! max와 min으로 가능하다
def solution(sizes):
    width = []
    height = []
    for size in sizes:
        width.append(max(size))
        height.append(min(size))
    w = max(width)
    h = max(height)
    return w*h

#3rd try
#사실상 리스트도 필요없다
def solution(sizes):
    #sizes에 있는 모든 길이를 하나의 리스트에 넣기
    w = max(sum(sizes,[]))
    #길이 쌍의 작은 수들 중 가장 큰 길이
    h = max([min(size) for size in sizes])
    return w*h
