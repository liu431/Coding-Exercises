class RandomizedSet:
    import random
    def __init__(self):
        self.rset = {}

    def insert(self, val: int) -> bool:
        if val in self.rset:
            self.rset[val] += 1
            return False
        else:
            self.rset[val] = 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.rset:
            self.rset.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        elements = list(self.rset.keys())
        return random.choice(elements)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
