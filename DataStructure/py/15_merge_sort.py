# 병합 정렬, merge sort (P.277)

#6-15) 병합 정렬 알고리즘
from typing import Sequence, MutableSequence

def merge_sort(a: MutableSequence) -> None:
    def _merge_sort(a:MutableSequence, left:int, right:int) -> None:
        if left < right:    #2개 이상부터 정렬 (원소가 1개면 if문 패스)
            center = (left+right)//2
            _merge_sort(a, left, center)
            _merge_sort(a, center+1, right)

            p = j = 0
            i = k = left

            # a의 전반부를 buff에 복사
            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1
            # buff에 복사된 a의 전반부와 a의 후반부를 비교하며 a에 저장
            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            #buff에 남은 전반부 원소가 있을 경우 (전반부 원소가 후반부 원소보다 큰게 있을 경우)
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
    n = len(a)
    buff = [None] * n   #작업용 임시 배열 생성
    _merge_sort(a, 0, n-1)
    del buff            #작업용 임시 배열 제거
