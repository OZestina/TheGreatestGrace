#https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3

#1st try
def solution(phone_number):
    a = len(phone_number)
    
    answer = '*' * (a-4) + phone_number[-4:]
    return answer
  
#2nd try
#가 필요없는 갓벽한 코드
