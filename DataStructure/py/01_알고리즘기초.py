#2021.10.19
#올바른 알고리즘이란 
#어떤 경우에도 실행 결과가 똑같이 나오는 것
#(대입값이 같은 경우일 때겠쥬?)

#1-1
print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a
if b > maximum : maximum = b
if c > maximum : maximum = c
print(f'최댓값은 {maximum}입니다.')


#1C-1
print('이름을 입력하세요: ', end = '')
name = input()
print(f'안녕하세요? {name}님.')

name = input('이름을 입력하세요: ')
print(f'안녕하세요? {name}님.')


#1C-2
def med3(a,b,c):
    if a >= b:
        if b >= c:
            return b
        elif a >= c:
            return c
        else:
            return a
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

#아래의 방법으로도 가능하지만, 중복되는 연산(b>=a, a<b 등)이 있어 효율적이지 않다
def med3_2(a,b,c):
    if (b>= a and a >=c) or (c>=a and a >= b):
        return a
    elif (a > b and b > c) or (c > b and b> a):
        return b
    else:
        return c 
      
      
#1-6: 삼항연산자 if ~ else
x = 3
y = 42
a = x if x > y else y
print(a)

c = 1
print('c는 0입니다' if c==0 else 'c는 0이 아닙니다')


#1-7
n = int(input('n값을 입력하세요: '))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f'1부터 {n}까지 정수의 합은 {sum}입니다')
print(f'i값은 {i}입니다')

#가우스 덧셈
print(n*(n+1)//2)       #이게되네


#1-12
n = int(input('출력할 +, -의 개수: '))
print('+-' * (n//2), end="")
if n%2 == 1: print("+")
    
    
#1-14
#*을 n개 출력, w개마다 줄바꿈하기

n = int(input('n 입력: '))
w = int(input('w 입력: '))

for _ in range(n//w):
    print('*' * w)
print("*" * (n%w))

while n > w:
    for _ in range(w):
        print("*", end="")
    n -= w
    print()
for _ in range(n):
    print("*", end="")
