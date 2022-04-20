# 이진검색트리 (P.382)
# 9-1)
from __future__ import annotations
from typing import Any

class Node:
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        #생성자
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    #이진 검색 트리

    def __init__(self):
        self.root = None

    def search(self, key: Any) -> Any:
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key > p.key:
                p = p.right
            else:
                p = p.left

    def add(self, key: Any, value: Any) -> bool:
        #Node의 값을 key, value로 뿌셔서 받음

        def add_node(node:Node, key: Any, value: Any) -> bool:
            #node를 루트로 하는 서브트리에 Node(key-value)를 삽입
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value)
                else:
                    #재귀로 처리
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value)
                else:
                    #재귀로 처리
                    add_node(node.right, key, value)
            return True

        if self.root is None:
            #빈 트리일 경우
            self.root = Node(key, value)
            return True
        else: return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        p = self.root
        parent = None
        is_left_child = True    #p가 parent의 왼쪽 자식 노드인지 확인 (False일 경우 오른쪽 자식이므로 변수 필요없!)

        while True:
            if p is None:   #더 이상 진행할 수 없으면
                return False

            if key == p.key:
                break       #검색 성공
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right
        #자식 하나인 경우
        if p.left is None:  #p에게 왼쪽 자식이 없으면 (자식 수 0~1)
            if p is self.root:
                self.root = p.right #오른 자식도 없으면 그냥 None이 들어감!
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        #자식 둘인 경우
        else:
            parent = p
            left = p.left   #가장 큰 노드 left 검색
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False
            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left

        return True

    def dump(self, reverse = False) -> None:

        def print_subtree(node: Node):
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key} {node.value}')
                print_subtree(node.right)

        def print_subtree_rev(node: Node):
            if node is not None:
                print_subtree_rev(node.right)
                print(f'{node.key} {node.value}')
                print_subtree_rev(node.left)

        print_subtree_rev(self.root) if reverse else print_subtree(self.root)

    def min_key(self) -> Any:
        if self.root is None:
            return None

        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        if self.root is None:
            return None

        p = self.root
        while p.right is not None:
            p = p.right
        return p.key
