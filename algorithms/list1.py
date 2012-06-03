# singly-linked lists

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
L = Node(1, Node(2, Node(3, Node(4, None))))
print L.value
print L.next.value
print L.next.next.value
print L.next.next.next.value