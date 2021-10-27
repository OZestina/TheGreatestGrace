#2021.10.27

#1-16
print('1부터 n까지 정수의 합 구하기')
while True:
    n = int(input('n값을 입력하세요>>'))
    if n > 0:
        break
    print('0보다 큰 정수를 입력하세요')
sum = 0
for i in range(n+1):
    sum += i
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#1-17
area = int(input('직사각형의 넓이를 입력하세요: '))
for i in range(1, area+1):
    if i * i > area : break
    if area % i : continue
    print(f'{i} x {area // i}')

# 1-18
import random
n = int(input('난수의 개수 입력: '))
for _ in range(n):
    r = random.randint(10,99)
    print(r, end=' ')
    if r == 13:
        print('\n프로그램을 중단합니다')
        break
else:                                   #break로 while/for문 종료 시 실행 안됨
    print('\n난수 생성을 종료합니다.')

# 1-20
for i in list(range(1,8)) + list(range(9,13)):  #리스트 생성 및 리스트 더하기..!
    print(i, end=' ')
print()

# 1-22
n = int(input('짧은 변의 길이를 입력하세요>> '))
for i in range(n):
    print('*' * (i+1))

# 1-23
n = int(input('짧은 변의 길이를 입력하세요>> '))
for i in range(n):
    print(f'{"*" * (i+1):>{n}}')

# 1C-4
n = 1
def put_id():
    x = 1
    print(f'id(x) = {id(x)}')
print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()
