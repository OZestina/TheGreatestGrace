#6-1) 버블 정렬 알고리즘
from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                

#6-3) 버블 정렬 알고리즘_개선1
#교환 횟수에 따른 중단 (교환이 일어나지 않으면 == 정렬이 완료됐으면 중단)
from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    # count = 0
    for i in range(n-1):
        count += 1
        exchng = 0
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        if exchng == 0:
            break
    # print(count)
    
    
#6-4) 버블 정렬 알고리즘_개선2
#스캔 범위 제한에 따른 (이미 정렬된 부분이 있으면 제외하고 정렬 시행)
from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    #count = 0
    while k < n-1:
        last = n-1
        #count += 1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last
    #print(count)
    
    
#6-5) 셰이커 정렬
#한 반복에 뒤->앞, 앞->뒤의 정렬을 실행해서 정렬 연산 수 단축
from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a)-1
    last = right
    # count = 0
    while left < right:
        # count += 1
        #뒤에서 앞으로 스캔
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last
        #앞에서 뒤로 스캔
        for j in range(left, right):
            if a[j] > a[j+1]:
                a[j +1], a[j] = a[j], a[j + 1]
                last = j
        right = last
    # print(count)
