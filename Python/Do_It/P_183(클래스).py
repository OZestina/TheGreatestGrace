class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result+= num
        return self.result

    def sub(self,num):
        self.result -= num
        return self.result

class FourCal:
    #생성자는 __init__ 으로 정의
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2

#class 클래스명(상속클래스이름)
class MoreFourCal(FourCal):
    def pow(self):
        result = self.num1 ** self.num2
        return result

#메서드 오버라이딩 (부모 클래스에 있는 메서드를 동일한 이름으로 다시 정의)
class SafeFourCal(FourCal):
    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2

#클래스변수
class Family:
    lastname = 'kim'

print(Family.lastname)
a = Family()

#같은 클래스일 경우 클래스 변수는 공유(주소값 같음)
print(id(a.lastname))
print(id(Family.lastname))
