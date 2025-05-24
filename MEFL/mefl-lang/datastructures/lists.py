# datastructures/lists.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def traverse(self, visit_func):
        current = self.head
        while current:
            visit_func(current.value)
            current = current.next

class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = DoublyNode(value)
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def traverse_forward(self, visit_func):
        current = self.head
        while current:
            visit_func(current.value)
            current = current.next

    def traverse_backward(self, visit_func):
        current = self.tail
        while current:
            visit_func(current.value)
            current = current.prev

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(0)
    print("Linked List traversal:")
    ll.traverse(print)

    dll = DoublyLinkedList()
    dll.append('a')
    dll.append('b')
    print("Doubly Linked List forward traversal:")
    dll.traverse_forward(print)
    print("Doubly Linked List backward traversal:")
    dll.traverse_backward(print)
