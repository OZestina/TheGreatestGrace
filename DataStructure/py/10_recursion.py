import math

#5-2) 유클리드 호제법으로 최대공약수 구하기
#GCD, Greatest Common Divisor, 최대공약수
def gcd(x:int, y:int) -> int:
    if y == 0:
        return x
    else:
        #둘 중 작은 수가 x로 들어와도 여기에서 gcd(y,x)로 바뀐다! 와 멋지다
        return gcd(y, x % y)

print(gcd(22,8))        #2
print(gcd(8,22))        #2

#기본 제공 함수는 math.gcd(x,y)
print(math.gcd(22,8))


#5-3)순수 재귀함수 구현
#재귀호출을 여러번 실행하는 함수 == 순수한(genuinely) 재귀
def recur(n: int) -> int:
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)

recur(4)        #1 2 3 1 4 1 2

#5-4)비재귀적으로 재귀 함수 구현 (while문)
def recur2(n: int) -> int:
    while n > 0:
        recur2(n-1)
        print(n)
        n = n-2

recur2(4)        #1 2 3 1 4 1 2

#5-5) 스택으로 재귀함수 구현
from collections import deque
def recur3(n: int) -> int:
    s = deque()
    while True:
        if n > 0:
            s.append(n)
            n = n-1
            continue
        if not(not s):  #s가 비어있지 않으면 (검색할 것이 있다면)
            n = s.pop()
            print(n)
            n = n-2
            continue
        break

recur3(4)       #1 2 3 1 4 1 2
