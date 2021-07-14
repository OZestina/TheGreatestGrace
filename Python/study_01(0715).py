# [예제로배우는파이썬프로그래밍] 기준 <반복문>까지 진행
# [빅데이터] 게시판 <1일차> 진행

number1 = input("나이 입력>> ") #문자로 인식
age = int(number1)
print("내년 나이는 ",age+1)

num1 = input("숫자1: ")
num2 = input("숫자2: ")
print("--------------")
n1 = int(num1)
n2 = int(num2)
print(n1,"과 ",n2,"의 합은 ",n1+n2,"입니다.")
print(n1,"과 ",n2,"의 곱은 ",n1*n2,"입니다.")

#파이썬은 +연산자를 이용해서 결합할 때 데이터의 타입이 동일해야 함
name = "홍길동"
age = 100
print(name+"의 나이는 "+str(age)+"입니다.")

name1 = input("이름 입력: ")
age1 = input("나이 입력: ")
print(name1,"님 환영합니다.")
print("당신의 나이는 ",age1, "세")

name2 = input("당신의 이름은: ")
age2 = input("나이 입력: ")
gender = input("당신의 성별은: ")
hobby = input("당신의 취미는: ")
motto = input("당신의 좌우명은: ")
print(name2+"은 "+age2+"세이고, "+gender+"이고 "+hobby+"가 취미이고")
print(motto+"라는 좌우명을 가지고 살아간다.")

nu1 = 33 #int로 인식
nu2 = 4 #int로 인식
print('나누기/(총값)>> ', nu1/nu2)
print('나누기/(몫)>> ', nu1//nu2)
print('나누기%(나머지)>> ', nu1%nu2)

coffee = input("커피값 입력: ")
count = input("커피 인원 수: ")
sum=int(coffee)*int(count)
if sum>=20000:
    print("2000원을 할인해드립니다.")
    print("금액:",sum-2000)
else:
    print("계산값을 다 지불하셔야합니다.")
    print("금액:", sum)

money = input ("1년 만기 정기 예금을 얼마나 예치하시겠습니까? ")
print("원금이 "+money+"원이시군요!")
print("이자는 ", int(money)/10, "원입니다.")
print("원리합계는 ", int(money)+int(money)/10, "원입니다.")

eng = int(input("영어점수 입력: "))
math = int(input("수학점수 입력: "))
kor = int(input("국어점수 입력: "))
print("=================")
print("세 과목의 합은",eng+math+kor)
print("세 과목의 평균은",(eng+math+kor)/3)

time = int(input("지금은 몇 시 입니까? "))
if time <12:
    print("점심 전입니다. 맛있게 드세요!")
else:
    print("점심 후입니다.")

id = input("로그인할 id를 입력>> ")
if id=="root":
    print("로그인 되었습니다.")
else:
    print("로그인되지 않았습니다.")

