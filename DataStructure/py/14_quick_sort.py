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


#6-11)
from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    x = a[(left+right) // 2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if right > pl: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a)-1)

    
#6-12)
#비 재귀적인 퀵 정렬 구현
#검사해야 할 pl, pr 좌표를 스택에 저장해 진행
#Stack은 하기 링크의 Stack 클래스를 사용한 것
#https://github.com/OZestina/TheGreatestGrace/blob/master/DataStructure/py/08_stack_collection.deque.py
from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    range = Stack(right-left+1)
    range.push((left, right))

    while not range.is_empty():
        pl, pr = left, right = range.pop()
        x = a[(left, right) // 2]

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: range.push((left, pr))
        if pl < right: range.push((pl, right))
            
            
            
#6-13)
# 퀵은 퀵인데 원소 수 9개 미만이면 단순 삽입 정렬로 진행
# (퀵정렬은 원소 수가 적은 경우에는 그다지 빠르지 않다고 함)

from typing import MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int) -> int:
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx2], a[idx3] = a[idx3], a[idx2]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    # 원소 수 9개 미만 용 단순 삽입 정렬
    for i in range(left+1, right+1):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
    # 원소 수 9개 이상용 퀵 정렬
    if right - left < 9:
        insertion_sort(a, left, right)
    else:
        pl = left
        pr = right
        m = sort3(a, pl, (pl+pr)//2, pr)
        x = a[m]

        a[m], a[pr-1] = a[pr-1], a[m]
        pl += 1
        pr -= 2
        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        if left < pr: qsort(a, left, pr)
        if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a)-1)
