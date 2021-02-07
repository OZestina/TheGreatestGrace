https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    search = "Kim"
    count = 0
    for i in seoul:
        if i == search:
            break
        else:
            count = count + 1
    answer = "김서방은 %d에 있다"
    return answer %count
    
# 서울에서 김서방 찾기ㅎㅎ
# answer 안에 변수 어떻게 넣는 지 잊어버려서 찾아서 함! (그거 빼고는 괜춘)
# 코딩 너무 오랜만에 해서 응용력 떨어진게 느껴진다^^ㅎㅎ
