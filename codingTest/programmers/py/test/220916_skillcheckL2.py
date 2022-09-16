# https://programmers.co.kr/skill_checks/418561

#Q1: 땅따먹기 게임
def solution(land):
    
    if len(land) == 1:
        return max(land[0])
    
    for stage in range(len(land)-2, -1, -1):
        for score in range(0, 4):
            temp = max(land[stage+1][0:score] + land[stage+1][score+1:])
            land[stage][score] += temp

    return max(land[0])
  
  
#Q2: 전화번호 접두어
#sort한 후 바로 뒤에거랑만 비교하면 되는거였당
def solution(phone_book):
    answer = True
    
    phone_book.sort()
    for n in range(len(phone_book)-1):
        for i in range(len(phone_book[n])):
            if phone_book[n][i] != phone_book[n + 1][i]:
                break
            if i == len(phone_book[n]) - 1:
                return False
    return answer
