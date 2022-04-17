# 원형 이중 연결 리스트 (원형 리스트 + 이중 연결 리스트) (P.356)
# 8-5)
from __future__ import annotations
from typing import Any

class Node:
    #원형 이중 연결 리스트용 노드 클래스

    def __init__(self, data: Any = None, prev: Node = None, next: Node = None) -> None:
        self.data = data
        self.prev = prev or self
        self.next = next or self

class DoubleLinkedList:
    #원형 이중 연결 리스트 클래스

    def __init__(self) -> None:
        self.head = self.current = Node()
        self.no = 0

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        # return self.no == 0
        return self.head.next is self.head  #next가 스스로를 참조하는가

    
