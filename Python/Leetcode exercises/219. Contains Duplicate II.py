class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Initialize the hash map
        dic = {}
        # Sliding window
        for ind, num in enumerate(nums):
            # If condition when it sees the seen num
            if num in dic and ind - dic[num] <= k:
                return True
            # Add the new num to the dic
            dic[num] = ind
        return False
        
                
        
