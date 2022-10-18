# https://school.programmers.co.kr/learn/courses/30/lessons/131130


# 1st try
def solution(cards):
    group = []
    while max(cards) != 0:
        start = max(cards)
        count = 0
        while cards[start - 1] != 0:
            temp = start - 1
            start = cards[temp]
            cards[temp] = 0
            count += 1
        group.append(count)
        
    if len(group) == 1:
        return 0
    group = sorted(group, reverse=True)
    return group[0] * group[1]
