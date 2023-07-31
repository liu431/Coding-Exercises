class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aSum = sum(aliceSizes)
        bSum = sum(bobSizes)
        equal = (aSum + bSum) / 2
        aDelta = equal - aSum
        for i, size in enumerate(aliceSizes):
            targetEx = int(size + aDelta)
            if targetEx in bobSizes:
                return [size, targetEx]
            
