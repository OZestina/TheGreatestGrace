# https://school.programmers.co.kr/learn/courses/30/lessons/148653#

# 1st try
# 1~4는 항상 아래로, 6~9는 항상 위로. 그럼 5는 언제 위로 올리고 언제 아래로 내려야할까?
#                                       => 5의 앞 숫자(5보다 큰 자리의 수)가 5 이상일 때 (ex) 56, 59, 555
def solution(storey):
    answer = 0
    temp = ''
    
    for i in str(storey):
        if int(i) < 5:
            answer += int(i)  # 내리는 수는 그냥 더해준다
            temp += ' '       # 추후 split 기준점
        else:
            temp += i
    
    floors = temp.split()
    for floor in floors:
        if floor == '5':      # 5일때는 내리는게 빠름 (올리면 6개가 들어간다)
            answer += 5
        else:                 # 큰 수로 만든 후 한 번에 내려오는 수 계산
            f = 10 ** len(floor) - int(floor)
            for i in str(f):
                answer += int(i)
            answer += 1       # 큰 수를 만든 후 한 번에 내려오는 것
    
    return answer
  
  
  
# 2nd try (다른 사람의 풀이)
# 재귀를 사용해도 되더라
def lift(floor):
    if floor < 10:
        return min(floor, 11 - floor)
    left = floor % 10
    return min(left + lift(floor // 10), 10 - left + lift(floor // 10 + 1))

def solution(storey):
    answer = lift(storey)
    return answer
