# https://programmers.co.kr/learn/courses/30/lessons/42577

#1st try
#효율성테스트 모두 fail. for문 한 번만 쓰게 줄여야한다
#n=len(phone_book), m=번호의평균길이 라고 했을때 복잡도는 n*n*m
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
#phone_book을 set로 만들어서 search를 O(1)로 만들어주면 n*m의 복잡도로 줄일 수 있다
#Set을 사용하지 않고 배열로 진행했을 때(24번줄 대신 25번줄 사용)는 효율성테스트 fail(2/4 성공)한다
def solution(phone_book):
    answer = True
    phoneSet = set(phone_book)
    for phoneNum in phone_book:
        for i in range(len(phoneNum)-1):
            if phoneNum[:i+1] in phoneSet:
            # if phoneNum[:i+1] in phone_book:
                answer = False
                break
    return answer

#다른 사람의 풀이. 소요시간 거의 1/5로 단축 (가장 오래걸리는 케이스 기준)
#와... 똑똑하다....
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False
    return True
