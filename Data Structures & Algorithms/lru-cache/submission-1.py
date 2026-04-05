class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            if node == self.head: return node.value
            if node.prev: node.prev.next = node.next
            if node.next: node.next.prev = node.prev
            if node == self.tail: self.tail = node.prev
            node.next = self.head
            node.prev = None
            if self.head: self.head.prev = node
            self.head = node
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.hm[key].value = value
            self.get(key)
            return
        if len(self.hm) == self.capacity:
            remove = self.tail 
            if remove.key in self.hm: del self.hm[remove.key]
            self.tail = remove.prev
            if self.tail: self.tail.next = None
            else: self.head = None
        node = Node(value, key)
        if not self.tail: self.tail = node
        node.next = self.head
        if self.head: self.head.prev = node
        self.head = node
        self.hm[key] = node