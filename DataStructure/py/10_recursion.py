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


#5-6) 하노이의 탑 구현
#no는 원반 개수, x는 시작기둥, y는 목표기둥
def move(no: int, x: int, y: int) -> None:
    if no > 1:
        move(no-1, x, 6-x-y)
    print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다')
    if no > 1:
        move(no-1, 6-x-y, y)

move(3,1,3)


#5-9) 8퀸문제
pos = [0]*8
flag_a = [False] * 8  #각 행 퀸 배치여부 확인
flag_b = [False] * 15  #대각선방향에 퀸 배치여부 확인
flag_c = [False] * 15  #대각선방향에 퀸 배치여부 확인


def put() -> None:  #출력
    # for i in range(8):
    #     print(f'{pos[i]:2}', end='')
    # print()
    for j in range(8):
        for i in range(8):
            print('■' if pos[i]==j else '□', end='')
        print()
    print()


def set(i:int) -> None: #i열에 퀸 배치
    for j in range(8):
        if (    not flag_a[j]
            and not flag_b[i+j]
            and not flag_c[i-j+7]):
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False

set(0)
