class MyHashSet:

    def __init__(self):
        self.hs = []

    def add(self, key: int) -> None:
        if key not in self.hs:
            self.hs.append(key)

    def remove(self, key: int) -> None:
        if key in self.hs:
            self.hs.remove(key)        

    def contains(self, key: int) -> bool:
        return key in self.hs
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
