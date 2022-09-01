from bisect import bisect

class RecentCounter:

    def __init__(self):
        self.requests = []
        self.len = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.len += 1
        #return sum([i >= t - 3000 for i in self.requests])\
        return self.len - bisect(self.requests, t - 3000) + (t-3000 in self.requests)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
