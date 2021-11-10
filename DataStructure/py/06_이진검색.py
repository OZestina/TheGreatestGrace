#2021.11.10

#이진검색, binary search
#검색대상 배열이 오름차순으로 정렬돼있어야 함

#복잡도, complexity
#시간복잡도(time), 공간(space)

#3-4
from typing import Any, Sequence
def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl+pr)//2
        if a[pc] == key:
            return pc       #검색 성공
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl == pr:
            return -1

print(bin_search([1,2,4,5,6],3))            #-1


#3C-3: 이진검색 알고리즘 실행과정 출력
from typing import Any, Sequence
def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    print('   |', end='')
    for i in range(len(a)):
        print(f'{i:4}', end="")
    print()
    print('---+' + (4*len(a)+2) * '-')

    while True:
        pc = (pl+pr)//2
        print('   |',end="")
        if pl != pc:
            print((pl*4+1)*' ' + '<-' + ((pc-pl)*4)*' ' + "+", end='')
        else:
            print((pc*4+1)* ' ' + '<+', end='')
        if pr != pc:
            print(((pr-pc)*4-2)*' ' + '->')
        else:
            print('->')
        print(f'{pc:3}|', end = '')
        for i in range(len(a)):
            print(f'{a[i]:4}', end='')
        print('\n   |')

        if a[pc] == key:
            return pc       #검색 성공
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl == pr:
            return -1

print(bin_search([1,2,4,5,6],5))            #3

#    |   0   1   2   3   4
# ---+----------------------
#    | <-        +      ->
#   2|   1   2   4   5   6
#    |
#    |             <+  ->
#   3|   1   2   4   5   6
#    |
