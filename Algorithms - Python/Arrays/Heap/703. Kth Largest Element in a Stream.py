class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        # heap only keep the top k elements
        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, i)
            else:
                if i > self.heap[0]:
                    heapq.heappushpop(self.heap, i)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            # add to heap
            heapq.heappush(self.heap, val)
        else:
            # insert new val and remove smallest element
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)      
        return self.heap[0]


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
