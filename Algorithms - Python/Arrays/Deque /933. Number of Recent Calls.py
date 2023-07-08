class RecentCounter:

    def __init__(self):
        self.requests = deque()


    def ping(self, t: int) -> int:
        self.requests.append(t)

        # remove requests that is older than 3000 milliseconds 
        while self.requests[0] + 3000 < t:
            self.requests.popleft()

        return len(self.requests)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
