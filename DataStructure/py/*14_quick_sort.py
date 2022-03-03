#quick sort (P.255)

#6-10)
from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n-1
    x = a[n//2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'피벗은 {x}입니다')

    print('피벗 이하인 그룹입니다')
    print(*a[0:pl]) #value만 출력할 때는 앞에 *를 붙여준다
    print(a[0:pl])

    #

if __name__ == '__main__':
    print('배열을 나눕니다')
    num = int(input('원수 수 입력: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)
