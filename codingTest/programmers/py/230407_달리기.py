# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# 1st try
# 상당히 느리다
def solution(players, callings):
    #각 선수들의 순서를 딕셔너리로 저장
    rank = dict()
    for i in range(len(players)):
        rank[players[i]] = i
    #선수 위치 변경, 딕셔너리 내 순서 변경
    for call in callings:
        fast, slow = call, players[rank[call] - 1]
        players[rank[call] - 1], players[rank[call]] = players[rank[call]], players[rank[call] - 1]
        rank[call] -= 1
        rank[slow] += 1
    
    return players
  
  
# 2nd try
# 값을 ++, -- 하는 것보다 값을 얹어주는게 더 빠르다..!
def solution(players, callings):
    #각 선수들의 순서를 딕셔너리로 저장
    rank = dict()
    for i in range(len(players)):
        rank[players[i]] = i

    #선수 위치 변경, 딕셔너리 내 순서 변경
    for call in callings:
        slow = players[rank[call] - 1]
        players[rank[call] - 1], players[rank[call]] = players[rank[call]], players[rank[call] - 1]
        rank[call], rank[slow] = rank[slow], rank[call]
    
    return players
