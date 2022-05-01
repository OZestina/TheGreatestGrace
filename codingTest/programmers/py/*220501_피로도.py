# https://programmers.co.kr/learn/courses/30/lessons/87946#

# 1st try => 17/19 성공
# 모두 다 하기는 싫으니 아래의 케이스가 통과하는 방법이 있는 지 찾아보자
# 100, [[100, 80], [20, 10], [20, 10], [20, 10], [20, 10]]
def solution(k, dungeons):
    # order = sorted(dungeons, key = lambda x: (x[1]-x[0], -x[0]))
    order = sorted(dungeons, key = lambda x: (x[1]-x[0], x[1], -x[0]))
    answer = 0
    print(order)
    for i in order:
        if k >= i[0]:
            k -= i[1]
            answer += 1
    
    return answer
