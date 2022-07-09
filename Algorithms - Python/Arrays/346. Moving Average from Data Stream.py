class MovingAverage:

    def __init__(self, size: int):
        self.arr = []a
        self.size= size
        

    def next(self, val: int) -> float:
        self.arr.append(val)
        window = min(len(self.arr), self.size)
        return sum(self.arr[-window:])/window


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
