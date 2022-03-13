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
    print(*a[0:pl])

    if pl > pr+1:
        print('피벗과 일치하는 그룹입니다')
        print(*a[pr+1:pl])ㅇㅇ

    print('피벗 이상인 그룹입니다')
    print(*a[pr+1 : n])

