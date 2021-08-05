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
    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        result = self.num1 + self.num2
    def sub(self):
        result = self.num1 - self.num2
    def mul(self):
        result = self.num1 * self.num2
    def div(self):
        result = self.num1 / self.num2
