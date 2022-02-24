#straight selection sort, 단순선택정렬 (P.237)
#가장 작은 원소부터 선택해 알맞은 위치로 옮기는 작업을 반복&정렬하는 알고리즘

#6-6)
from typing import MutableSequence
def selection_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if a[j] < a[min]:
                min = j
        a[i],a[min] = a[min],a[i]


#straight insertion sort, 단순삽입정렬(P.240)
#주목한 원소보다 더 앞쪽에서 알맞은 위치로 삽입하며 정렬 (배열에 저장된 수들의 순서대로 자리를 찾아줌)

#6-7)
from typing import MutableSequence
def insertion_sort(a:MutableSequence) -> None:
    n = len(a)
    for i in range(1,n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp
        
#6C-1) 이진 삽입 정렬 알고리즘: 검색 단축
from typing import MutableSequence
def binary_sort(a:MutableSequence) -> None:
    n = len(a)
    for i in range(1,n):
        key = a[i]
        pl = 0
        pr = i - 1

        while True:
            pc = (pl+pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j-1]
        a[pd] = key
        
#6C-2) 이진 삽입 정렬 알고리즘 bisect.insort로 사용
from typing import MutableSequence
import bisect

def binary_insertion_sort(a:MutableSequence) -> None:
    for i in range(1, len(a)):
        bisect.insort(a,a.pop(i),0,i)
