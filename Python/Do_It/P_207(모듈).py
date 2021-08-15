import mod1

a = mod1.add(3,4)
print(a)

b = mod1.sub(4,3)
print(b)
#-------------------------------------------
#mod2.py
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)


def add(a, b):
    return a + b
#-------------------------------------------

# calculator 모듈에 있는 모든 것(*)을 import 하겠다
# 이렇게 하면 calculator.함수명 대신 함수를 바로 사용할 수 있다
from calculator import *
import mod2

print(add(3, 4))

print(mod2.PI)
a = mod2.Math()
print(a.solv(2))

#왜 아래에는 solv에 self값도 넣어줘야하지..?
print(mod2.Math.solv(0,2))

print(mod2.add(3,4))

