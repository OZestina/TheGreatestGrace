# https://school.programmers.co.kr/learn/courses/30/lessons/155651

# 1st try
def room_occu(slot, start, end):
    st_min = int(start[:2]) * 60 + int(start[3:])
    end_min = int(end[:2]) * 60 + int(end[3:]) + 10 #청소시간 추가
    if end_min > 1439:
        end_min = 1439
    for i in range(st_min, end_min):
        slot[i] += 1
    

def solution(book_time):
    # 각 분마다 필요한 방 count용
    slot = [0 for _ in range(60 * 24)]
    
    for start, end in book_time:
        room_occu(slot, start, end)
    
    return max(slot)
  
  
  
# 2nd try (다른 사람 풀이 참고)
# start, end 만 별도 표시해주고 누적합으로 푸는 방법이 있었다! => 계산을 위한 for문을 한 번만 도는 셈
def solution(book_time):
    # 각 분마다 필요한 방 count용
    slot = [0] * (60 * 24)
    
    # 시작시간에 +1, 마침시간에 -1
    for start, end in book_time:
        st_min = int(start[:2]) * 60 + int(start[3:])
        end_min = int(end[:2]) * 60 + int(end[3:]) + 10 #청소시간 추가
        if end_min > 1439:
            end_min = 1439
        slot[st_min] += 1
        slot[end_min] -= 1
    
    # slot 누적합 계산
    for i in range(1, 1440):
        slot[i] += slot[i - 1]
    
    return max(slot)
