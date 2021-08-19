# 출제문제: 계좌를 만드는 모듈을 만들어 실행해 봅시다

# [모듈(Account.py) 내 저장할 것들]
# 1) Account 클래스 생성
# > 입력값을 이름(str), 계좌번호(str), 금액(int)으로 한 생성자를 만드세요
#
# 2) Account 클래스를 상속받는 자식 클래스 2개 생성
# > AccountNormal
# 	- 클래스 변수 (상수) RATE (double, 0.01)
# 	- 총 보유 금액 출력 메서드 (금액 * rate)
# > AccountVip
# 	- 클래스 변수 (상수) RATE (double, 0.1)
# 	- 총 보유 금액 출력 메서드 (금액 * rate)
#
# 3) Account.py 파일을 실행하면 하기 파일이 출력되도록 하자
# "이 파일은 모듈입니다. 다른 파일에서 import하여 사용해주세요"
# (import하여 사용 시 위의 문구는 출력되지 않는다)

# [실행파일]
# 4) 다른 파이썬 파일에서 Account.py를 import해 AccountNormal과 AccountVip 객체를 하나씩 만들고, 메서드를 사용해 총 보유 금액을 각각 출력해보세요

#Account.py
class Account:
    def __init__(self, name, number, money):
        self.name = name
        self.number = number
        self.money = money

class AccountNormal(Account):
    RATE = 0.01
    def AccountPrint(self):
        print(str(self.number)+"의 잔고는 현재 "+str(int((1+AccountNormal.RATE)*self.money))+"원입니다")

class AccountVip(Account):
    RATE = 0.1
    def AccountPrint(self):
        print(str(self.number)+"의 잔고는 현재 "+str(int((1+AccountVip.RATE)*self.money))+"원입니다")

if __name__ == "__main__":
    print("이 파일은 모듈입니다. 다른 파일에서 import하여 사용해주세요")

#main.py
from Account import *

n1 = AccountNormal("김영희", "12345", 10000)
v1 = AccountVip("김민희", "23456", 10000)

n1.AccountPrint()
v1.AccountPrint()    
    
# =====================================================================================
# 1
# 1. 연락처 관리 프로그램 UI
#    1. 친구 리스트 출력
#    2. 친구 추가
#    3. 친구 삭제
#    4. 이름 변경
#    9. 종료
#    메뉴를 선택하세요 >>
#   -------------------------
# 2. 친구를 추가하시고 출력하세요. => 홍길동, 임길동
# 3. 친구 이름을 변경하시고 출력하세요. => 임길동 -> 임꺽정
# 4. 친구를 삭제하시고 출력하세요 => 홍길동
# 5. 마지막에 시스템을 종료하세요.
friends = []
while(True):
    print("1. 친구 리스트 출력\n2. 친구 추가\n3. 친구 삭제\n4. 이름 변경\n9. 종료")
    choice = input("메뉴를 선택하세요 >> ")
    if choice == "1":
        print(friends)
    elif choice == "2":
        new = input("새 친구 이름을 입력하세요 >> ")
        friends.append(new)
    elif choice == "3":
        delete = input("절교할 친구 이름을 입력하세요 >> ")
        if delete in friends:
            friends.remove(delete)
    elif choice == "4":
        oldName = input("이름을 바꾼 친구 이름을 입력하세요 >> ")
        if oldName in friends:
            newName = input("친구의 새 이름을 입력하세요 >> ")
            friends[friends.index(oldName)] = newName
        else:
            print("그런 친구는 없네요")
    elif choice == "9":
        break
    else:
        pass

# 2
# 세미나에 참석한 사람들 명단이 세트 A와 B에 있다. 2개의 파티 모두 참석한 사람을 출력하시오.
# 세미나 A: 홍길동, 김길동, 박길동, 정길동
# 세미나 B: 홍길동, 박길동, 황길동
listA = ["홍길동", "김길동", "박길동", "정길동"]
listB = ["홍길동", "박길동", "황길동"]
listBoth = list(set(listA) & set(listB))
print(listBoth)

# 3
# 이름과 나이를 속성으로 가진 강아지 클래스를 정의하라.
# 그리고 이름이 바둑이, 나이가 5살인 객체와 이름이 멍멍이, 나이가 7살인 객체를 생성하고 나이를 출력하시오.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Dog("바둑이", 5)
b = Dog("멍멍이", 7)
print(a.age)
print(b.age)

# 4
# class Person을 생성하고 이름과 주민 번호를 변수로 가지도록 정의하시오.
# Class Ceo를 생성하고 연봉을 변수로 추가해서 가지도록 정의하시오.
# CEO인 홍길동의 주민번호 앞자리는 901112이고 봉급은 천만원으로 해서 프린트하시오.
class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn
    def __str__(self):
        print("이름: "+self.name)
        print("주민번호: " + self.ssn)

class Ceo(Person):
    def __init__(self, name, ssn, salary):
        Person.__init__(self,name,ssn)
        self.salary = salary
    def __str__(self):
        Person.__str__(self)
        print("봉급: "+self.salary)

a = Ceo("홍길동", "901112", "천만원")
a.__str__()

#5
# tri.py
# triangle이라는 클래스를 만들어 객체 생성 후
# 메서드를 이용하여 삼각형인지 아닌지, 총 몇 개의 삼각형이 만들어졌는지 알려주세요.
# (예: triangle(90, 30, 60).check() >> 출력: 삼각형입니다.)
# (예: triangle(90, 90, 30).check() >> 출력: 삼각형이 아닙니다.)
# (예: triangle.count >> 1)
class Triangle:
    count = 0

    def __init__(self, d1, d2, d3):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def check(self):
        if self.d1 + self.d2 + self.d3 == 180:
            Triangle.count += 1
            print("삼각형입니다")
        else:
            print("삼각형이 아닙니다")

if __name__ == "__main__":
    Triangle(90,30,60).check()
    Triangle(90,90,60).check()
    print(Triangle.count)

#6
# tri2.py
# tri1.py의 triangle클래스를 상속받아 triangle2 클래스 생성 후 check()메서드를 재정의하세요.
# 객체 생성시 정삼각형인지 아닌지를 알려주세요.
# (예: triangle2(60, 60, 60).check() >> 출력: 정삼각형입니다.)
# (예: triangle2(90, 60, 30).check() >> 출력: 정삼각형이 아닙니다.)
# 앞서 tri.py에 실행했던 print 함수들은 tri2.py에서 실행되지 않게 해주세요.
class Triangle2(Triangle):
    def check(self):
        if self.d1 == 60 and self.d2 == 60 and self.d3 == 60:
            Triangle.count += 1
            print("정삼각형입니다")
        elif self.d1 + self.d2 + self.d3 == 180:
            Triangle.count += 1
            print("정삼각형이 아닙니다")
        else:
            print("삼각형이 아닙니다")

Triangle2(60,60,60).check()
Triangle2(90,30,60).check()
Triangle2(90,90,60).check()
print(Triangle.count)
