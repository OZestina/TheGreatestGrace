#배열의 맨 앞부터 순서대로 원소를 스캔
#원소의 값이 정렬되지 않은 배열에서 검색할때 사용

#3-2
from typing import Any, Sequence        #시퀀스는 임의의 자료형
def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

#3C-2
t = (4, 7, 5.6, 3.14, 1)
s = 'string'
a = ['BTS','AAC','MDN']
print(f'{t}에서 5.6의 인덱스는 {seq_search(t,5.6)}입니다')    #인덱스는 2입니다
print(f'{s}에서 n의 인덱스는 {seq_search(s,"n")}입니다')      #인덱스는 4입니다
print(f'{a}에서 "BTS"의 인덱스는 {seq_search(a,"BTS")}입니다')#인덱스는 0입니다

#보초법
#검색하고자 하는 key값을 배열의 맨 끝에 저장해 연산과정(if문) 줄임
from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)       #보초를 세운다
    
    i = 0
    while True:
        if a[i] == key:
            break       #언젠가는 보초를 만나게 되어있어!
        i += 1
    
    return -1 if i == len(seq) else i
