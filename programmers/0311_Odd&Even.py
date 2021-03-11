#https://programmers.co.kr/learn/courses/30/lessons/12937?language=python3#

#1st try
def solution(num):
    if num%2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer
  
#2nd try
#1 == True, 0 == False 인 점을 활용하면 아래와 같이도 표현 가능! (머시썽!)
# +) answer 변수도 생략 가능하여 없애봄
def solution(num):
    if (num%2) :
        return "Odd"
    else:
        return "Even"
      
#3rd try
#누군가가 풀어둔 비트연산자 '&'을 활용한 코드. 머씨썽!!!
#num에 대입되는 수의 크기에 상관없이 홀/짝을 구분하는 마지막 한 자리 수만 연산 가능하구나!

def solution(num):
    return ["Even","Odd"] [num & 1]
  
