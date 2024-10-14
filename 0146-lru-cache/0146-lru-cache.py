class Node:
    def __init__(self, left = None, right = None, key = 0, val = None):
        self.val = val 
        self.left = left
        self.right = right
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.dic = {}
        self.lru = Node() 
        self.mru = Node()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self.dic:
            temp = self.dic[key]
            temp.left.right = temp.right
            temp.right.left = temp.left
            self.mru.left.right = temp
            temp.right = self.mru
            temp.left = self.mru.left
            self.mru.left = temp
            return temp.val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if not len(self.dic):
            temp = Node(self.lru, self.mru, key, value)
            self.lru.right = temp
            self.mru.left = temp
            self.dic[key] = temp
        elif key in self.dic:
            self.dic[key].val = value
            temp = self.dic[key]
            temp.left.right = temp.right
            temp.right.left = temp.left
            self.mru.left.right = temp
            temp.right = self.mru
            temp.left = self.mru.left
            self.mru.left = temp
        elif len(self.dic) < self.capacity:
            temp = Node(self.mru.left, self.mru, key, value)
            self.mru.left.right = temp
            self.mru.left = temp
            self.dic[key] = temp
        else:
            self.dic.pop(self.lru.right.key)
            self.lru.right = self.lru.right.right
            self.lru.right.left = self.lru
            temp = Node(self.mru.left, self.mru, key, value)
            self.mru.left.right = temp
            self.mru.left = temp
            self.dic[key] = temp




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)