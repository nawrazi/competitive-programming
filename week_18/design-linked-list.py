# https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.nodes = []

    def get(self, index: int) -> int:
        if index >= len(self.nodes):
            return -1
        return self.nodes[index].val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if len(self.nodes) > 0:
            node.next = self.nodes[0]
        self.nodes = [node] + self.nodes

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if len(self.nodes) > 0:
            self.nodes[-1].next = node
        self.nodes.append(node)

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        if index > len(self.nodes):
            return
        elif index == len(self.nodes):
            self.addAtTail(val)
        else:
            self.nodes.insert(index, node)
            node.next = self.nodes[index+1]
            self.nodes[index-1].next = node

    def deleteAtIndex(self, index: int) -> None:
        if index >= len(self.nodes):
            return
        if index != 0:
            self.nodes[index-1].next = self.nodes[index].next
        self.nodes[index].next = None
        self.nodes.pop(index)
