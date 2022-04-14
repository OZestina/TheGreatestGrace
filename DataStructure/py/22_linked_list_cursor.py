# 연결리스트 w.커서 (P.343)
# 프리리스트(free list) 자료구조를 사용해 삭제된 레코드 그룹을 관리
# 8-3)
from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:
    def __init__(self, data = Null, next = Null, dnext = Null):
        self.data = data
        self.next = next
        self.dnext = dnext

class ArrayLinkedList:

    def __init__(self, capacity: int):
        self.head = Null
        self.current = Null
        self.max = Null         #사용중인 꼬리 레코드
        self.deleted = Null     #프리리스트의 머리 노드
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.no = 0

    def __len__(self) -> int:
        return self.no

    def get_insert_index(self):
        #다음에 삽입할 레코드의 인덱스를 구함
        if self.deleted == Null:
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max
            else:
                return Null
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext
            return rec

    def delete_index(self, idx: int) -> None:
        #레코드 idx를 프리리스트에 등록
        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].dnext = Null
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec

    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = self.n[ptr].next
        return Null

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= Null

    def add_first(self, data: Any):
        ptr = self.head
        rec = self.get_insert_index()
        print(rec)
        if rec != Null:
            self.head = self.current = rec
            self.n[rec] = Node(data, ptr)
            self.no += 1
        else:
            print('capacity 부족')

    def add_last(self, data: Any) -> None:
        if self.head == Null:
            self.add_first()
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()
            print(rec)

            if rec != Null:
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1
            else:
                print('capacity 부족')

    def remove_first(self) -> None:
        if self.head != Null:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1
        else:
            print('제거할 데이터가 없습니다')

    def remove_last(self) -> None:
        if self.head != Null:
            if self.n[self.head].next == Null:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head
                while self.n[ptr].next != Null:
                    pre, ptr = ptr, self.n[ptr].next
                self.n[pre].next = Null
                self.no -= 1
                self.current = pre
                self.delete_index(ptr)

    def remove(self, p: int) -> None:
        #레코드 p를 삭제
        if self.head != Null:
            if p == self.head:
                self.remove_first()
            else:
                ptr = self.head
                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return
                self.n[p].next = Null
                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.no -= 1
                self.current = ptr

    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head != Null:
            self.remove_first()
        self.current = Null

    def next(self) -> bool:
        if self.current == Null or self.n[self.head].next == Null:
            return False
        self.current = self.n[self.current].next
        return True

    def print_current_node(self) -> None:
        if self.current != None:
            print(self.n[self.current].data)
        else:
            print('주목 노드 없음')

    def print(self) -> None:
        ptr = self.head
        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) -> None:
        for i in self.n:
            print(f'[{i}] {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        return ArrayLinkedListIterator(self.n, self.head)


class ArrayLinkedListIterator:
    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data
