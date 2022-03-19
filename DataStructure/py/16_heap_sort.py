# 힙 정렬, heap sort (P.286)
# heap: '부모의 값이 자식의 값보다 항상 크다'는 조건을 만족하는 완전 이진 트리
# 그래서 힙에서 최댓값은 루트에 위치한다 - 는 특징을 이용해 정렬한다

#6-16)

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        temp = a[left]
        parent = left

        while parent < (right+1)//2:
            cl = parent*2 + 1
            cr = cl + 1

            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
            
        a[parent] = temp

    n = len(a)

    for i in range((n-1) // 2, -1, -1):
        down_heap(a, i, n-1)

    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)


        
# 6C-5) heapq 모듈 사용 힙정렬
# heappush(): 힙에 원소 추가
# heappop(): 힙에서 원소 제거

import heapq
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    heap = []
    for i in a:
        heapq.heappush(heap,i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)
