#2021.11.16

#3-5
from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None               #연결할 바로 앞의 노드 저장 (초기값은 hash)

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False    #key가 존재하지 않음

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()


#3-6
from enum import Enum
#from chained_hash import ChainedHash

Menu = Enum('메뉴',['추가','삭제','검색','덤프','종료']) #메뉴 선언

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]  #[<메뉴.추가: 1>, <메뉴.삭제: 2>, <메뉴.검색: 3>, <메뉴.덤프: 4>, <메뉴.종료: 5>]
    while True:
        print(list(Menu))
        print(*s, sep = '  ', end=': ')
        n = int(input())
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = ChainedHash(13)

while True:
    menu = select_menu()    #메뉴 선택 프린트

    if menu == Menu.추가:
        key = int(input('추가할 키 입력: '))
        val = input('추가할 값 입력: ')
        if not hash.add(key, val):  #추가해보고 False 값 나오면 print 실행
            print('추가 실패')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키 입력: '))
        if not hash.remove(key):
            print('삭제 실패')

    elif menu == Menu.검색:
        key = int(input('검색할 키 입력: '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키의 값: {t}')
        else:
            print('검색 실패')

    elif menu == Menu.덤프:
        hash.dump()

    else:
        break
