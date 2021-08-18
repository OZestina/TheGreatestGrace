#mod1.py를 import
import mod1

#from mod1 import add => add함수 모듈명없이 add로 바로 사용 가능
#from mod1 import *   => mod1에 속한 함수 모듈명없이 함수명으로 바로 사용 가능

#import한 모듈의 함수를 쓸 때는 모듈.함수명()으로 사용
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

#__name__ : 내부적으로 사용하는 특별한 변수로, 
#직접 실행하면 __main__으로,
#import돼 실행되면 (모듈로 실행되면) 모듈명(이 경우에는 mod2)으로 저장됨
if __name__ == "__main__":
    print("mod2.py를 실행합니다")
#-------------------------------------------

from calculator import *
import mod2

print(add(3, 4))

print(mod2.PI)
a = mod2.Math()
print(a.solv(2))

#왜 아래에는 solv에 self값도 넣어줘야하지..?
#self값은 객체명이 들어가는 곳인데, 객체 생성없이 바로 써서 그런가보다^^
print(mod2.Math.solv(0,2))

print(mod2.add(3,4))

