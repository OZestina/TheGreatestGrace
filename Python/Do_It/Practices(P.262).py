#Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

#Q2
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

#Q3
print(all([1,2, abs(-3) - 3]))    #False
print(chr(ord('a'))=='a')       #True

#Q4
lists = [1,-2,3,-5,8,-3]
print(list(filter(lambda x: x>0, lists)))

#Q5
print(hex(234))     #0xea
print(int('0xea',16))    #234

#Q6
print(list(map(lambda x: x*3, [1,2,3,4])))

#Q7
lists = [-8,2,7,5,-3,5,0,1]
print(max(lists) + min(lists))  #-1
