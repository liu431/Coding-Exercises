from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        '''Initialize the LRU cache with positive size capacity'''
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        '''Return the value of the key if the key exists, otherwise return -1'''
        if key not in self:
            return -1
        
        self.move_to_end(key)
        return self[key]
    
    def put(self, key: int, value: int) -> None:
        '''Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.'''
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
