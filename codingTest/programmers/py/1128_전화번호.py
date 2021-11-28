# https://programmers.co.kr/learn/courses/30/lessons/42577

#1st try
#효율성테스트 모두 fail. for문 한 번만 쓰게 줄여야한다
def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                answer = False
                break
    return answer
  
#2nd try
