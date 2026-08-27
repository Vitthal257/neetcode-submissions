class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next=None
        self.prev=None
    
    

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def insertAtEnd(self,A):
        oldMRU = self.mru.prev
        oldMRU.next = A
        A.prev = oldMRU
        A.next = self.mru
        self.mru.prev = A


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value  = self.cache[key]
        self.remove(value)
        self.insertAtEnd(value)
        return value.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            v = self.cache[key]
            v.val = value
            self.remove(v)
            self.insertAtEnd(v)
            return
        else:
            if len(self.cache)<self.cap:
                nn = Node(key, value)
                self.insertAtEnd(nn)
                self.cache[key] = nn
            else:
                nodetbr = self.lru.next
                del self.cache[nodetbr.key]
                self.remove(nodetbr)
                nn = Node(key,value)
                self.insertAtEnd(nn)
                self.cache[key] = nn



            


        
        

        
