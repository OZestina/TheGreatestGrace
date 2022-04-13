# 연결리스트 w. 포인터 (P.323)
# 8-1)
# 함수가 속한 클래스의 이름을 annotation하기 위해 import (line 9의 next: Node 부분)
from __future__ import annotations
from typing import Any, Type

class Node:
    #연결 리스트용 노드 클래스
    def __init__(self, data: Any = None, next: Node = None):
        self.data = data
        self.next = next

class LinkedList:
    #연결 리스트 클래스
    
    def __init__(self) -> None:
        #초기화
        self.no = 0
        self.head = None
        self.current = None
    
    def __len__(self) -> int:
        return self.no
    
    def search(self, data: Any) -> int:
        #data와 값이 같은 노드를 검색
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    
    def __contains__(self, data: Any) -> bool:
        #이 함수를 구현함으로써 연결 리스트에 in 연산자 적용 가능
        return self.search(data) >= 0
    
    def add_first(self, data: Any) -> None:
        #맨 앞에 노드 삽입
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1
        
    def add_last(self, data: Any) -> None:
        #맨 뒤에 노드 삽입
        if self.head is None:
            #리스트가 비어있는 경우
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1
                
    def remove_first(self) -> None:
        #머리 노드 삭제
        if self.head is not None:
            self.head = self.current = self.head.next
            self.no -= 1
        
    def remove_last(self):
        if self.head is not None:
            #리스트가 비어있지 않을 때
            if self.head.next is None:
                #노드가 1개일 경우
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head #ptr의 앞 노드를 가리킴
                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no -= 1
