# 도수정렬, counting sort (P.297)
# 분포수 세기, distribution counting

# 6-17) 도수 정렬 알고리즘 구현
from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    n = len(a)
    f = [0] * (max+1)
    b = [0] * n

    #도수분포표 만들기
    for i in range(n): f[a[i]] += 1
    #누적 도수분포표
    for i in range(1, max+1): f[i] = f[i] + f[i-1]
    #누적된 수에 따라 맞는 자리에 넣기
    for i in range(n-1, -1, -1): f[a[i]] -= 1; b[f[a[i]]] = a[i]
    #b를 a에 덮어씌우기
    for i in range(n): a[i] = b[i]

def counting_sort(a: MutableSequence) -> None:
    fsort(a, max(a))
