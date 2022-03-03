class MyHashMap:

    def __init__(self):
        self.maps = [[]]

    def put(self, key: int, value: int) -> None:
        for ind, val in enumerate(self.maps):
            if len(val) != 0 and key == val[0]:
                self.maps[ind][1] = value
                return None
        self.maps.append([key, value])
        return None
                

    def get(self, key: int) -> int:
        for ind, val in enumerate(self.maps):
            if len(val) != 0 and key == val[0]:
                return self.maps[ind][1]
        return -1        

    def remove(self, key: int) -> None:
        for ind, val in enumerate(self.maps):
            if len(val) != 0 and key == val[0]:
                self.maps.pop(ind)      


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
