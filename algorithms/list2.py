# a stack implemented using singly-linked lists

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
        
class Stack:
    def __init__(self, node):
        self.top = node
    
    def push(self, data):
        data.next = top
        self.top = data
    
    def pop(self):
        if not self.top:
            return None
        temp = self.top
        self.top = self.top.next
        return temp

S = Stack(Node('a', None))
print S.top.value
d = S.pop()
print d.value
print S.top