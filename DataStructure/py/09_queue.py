#2021.11.23

from typing import Any

class FixedQueue:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        for i in range(self.no):
            idx = (i+self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.no):
            idx = (i+self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0

    def clear(self) -> None:
        self.front = self.rear = self.no = 0

    def dump(self) -> None:
        if self.is_empty():
            print('queue is empty')
        else:
            for i in range(self.no):
                print(self.que[(i+self.front)%self.capacity], end=' ')
            print()

#let's use what we made
from enum import Enum
#from fixed_queue import FixedQueue

Menu = Enum('메뉴',['인큐','디큐','피크','검색','덤프','종료'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end=': ')
        n = int(input())
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f'현재 데이터 개수: {len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.인큐:
        x = int(input('데이터를 입력하세요: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('queue is already full', end='\n\n')

    elif menu == Menu.디큐:
        try:
            x = q.deque()
            print(f'팝한 데이터는 {x}입니다', end='\n\n')
        except FixedQueue.Empty:
            print('queue is already empty', end='\n\n')

    elif menu == Menu.피크:
        try:
            x = q.peek()
            print(f'피크한 데이터는 {x}입니다', end='\n\n')
        except FixedQueue.Empty:
            print('queue is already empty', end='\n\n')

    elif menu == Menu.검색:
        x = int(input('검색할 값을 입력하세요: '))
        if x in q:
            print(f'{q.count(x)}개 포함. 맨 앞의 위치: {q.find(x)}', end='\n\n')
        else:
            print('result not found', end='\n\n')

    elif menu == Menu.덤프:
        q.dump()

    else:
        break

