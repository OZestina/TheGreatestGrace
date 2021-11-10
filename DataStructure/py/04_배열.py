#2021.11.02

#from typing import Any, Sequence
#Any: 제약이 없는 임의의 자료형
#Sequence: 리스트, 튜플, range, 문자열처럼 값이 연속적으로 이어진 자료형
#함수 annotation: 함수의 매개변수와 반환값을 나타내는 역할 (강제성은 없음)

#enumerate(): 인덱스와 원소를 짝지어 튜플로 꺼내준다

#iterator(반복자): 데이터의 나열을 표현하는 객체
#iter(이터러블 객체)로 반환받을 수 있다
#__next__함수 호출 / next(이터레이터) 로 원소를 순차적으로 꺼낼 수 있다


#2-2
from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    #시퀀스형 a원소의 최댓값을 반환
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum: maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수 입력: '))
    #원소 수가 num인 리스트 생성 (초기값 None)
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] 값을 입력하세요: '))

    print(f'최댓값은 {max_of(x)}입니다.')

    
#2C-2
x = ['John','George','Paul','Ringo']
for i, name in enumerate(x):        #인덱스 0부터 시작
    print(f'x[{i}] = {name}')
for i, name in enumerate(x,1):      #enumerate() 인덱스 1부터 카운트
    print(f'x[{i}번째] = {name}')
for i, name in enumerate(reversed(x)):        #시퀀스 거꾸로!
    print(f'x[{i}] = {name}')


print(iter(x))          #<list_iterator object at 0x00B7CDD0>
print(list(iter(x)))    #list 반환

y = reversed(x)         #<list_reverseiterator object at 0x0171CE30>
y = list(reversed(x))   #list 반환

x.reverse()     #x를 역순으로 정렬 (원본을 바꿈)    


#2-7
#10의 정숫값 x를 r진수로 변환해 그 수를 나타내는 문자열로 반환
def card_conv(x: int, r: int) -> str:
    d = ''        #변환 후의 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #정렬을 위한 길이
    n = len(str(x))
    print(f'{r:2} | {x:{n}d}')

    while x > 0:
        d += dchar[x % r]
        x //= r     #x에 x를 r로 나눈 몫을 대입

    return d[::-1]  #d에 담긴 문자열을 역순으로 반환

x = input('enter x: ')
r = input('enter r: ')
print(card_conv(int(x),int(r)))


#2-9
counter = 0
prime = [2,3,5,7]

for n in range(9, 1001, 2):
    for i in prime:
        counter += 1
        if n % i == 0:
            break
    else:
        prime.append(n)

print(prime)
print(counter)      #15115

#2-10
counter = 0
prime = [2,3,5,7]

for n in range(9, 1001, 2):
    i = 1           #홀수만 계산하니까 2는 제외
    while prime[i]*prime[i] <= n:
        counter += 2    #곱셈이랑 나눗셈
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime.append(n)
        counter += 1

print(prime)
print(counter)      #3772


#얕은 복사(참조값만 복사)
x = [[1,2],[3,4]]
y = x.copy()
x[0][1] = 9
print(x)    #[[1, 9], [3, 4]]
print(y)    #[[1, 9], [3, 4]]

#깊은 복사는 deep
#copy 임포트 필요
import copy
x = [[1,2],[3,4]]
y = copy.deepcopy(x)
x[0][1] = 7
print(x)    #[[1, 7], [3, 4]]
print(y)    #[[1, 2], [3, 4]]
