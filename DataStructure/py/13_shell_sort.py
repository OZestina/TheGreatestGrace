#shell sort, 셸 정렬 (P.247)


#6-8)
from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    n = len(a)                          #(n==8) 가정
    h = n//2                            #(h==4)
    while h > 0:
        for i in range(h,n):            #i = 4,5,6,7
            j = i-h                     #j = 0,1,2,3
            tmp = a[i]                  #tmp = a[4,5,6,7]
            while j >= 0 and a[j] > tmp:#a[0,1,2,3]
                a[j+h] = a[j]           #a[4,5,6,7]=a[0,1,2,3]
                j -= h                  #-4,-3,-2,-1
            a[j+h] = tmp                #자리 바꿨을 경우 a[0,1,2,3] or 안바꿨을 경우 a[4,5,6,7]
        h //= 2                         #(h==2)


        
#6-9) 셸 정렬의 h는 서로 배수가 되지 않도록 해야 좋다
# => h * 3 + 1의 수열을 사용하도록 한 알고리즘
from typing import MutableSequence

def shell_sort2(a: MutableSequence) -> None:
    n = len(a)
    h = 1
    while h < n // 9:          # n < 9 일 경우 h = 1 로 진행됨
        h = h*3+1
    while h > 0:
        for i in range(h,n):
            j = i-h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 3
