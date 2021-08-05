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

class MoreFourCal(FourCal):
    def pow(self):
        result = self.num1 ** self.num2
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2

class Family:
    lastname = 'kim'

print(Family.lastname)
a = Family()

print(id(a.lastname))
print(id(Family.lastname))
