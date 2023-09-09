class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        while len(stones) > 1:
            heapq._heapify_max(stones)
            y = heapq._heappop_max(stones)
            x = heapq._heappop_max(stones)
            print(y, x)
            if x != y:
                y_new = y - x
                heapq.heappush(stones, y_new)
                print(stones)
        if stones:
            return stones[0]
        else:
            return 0
