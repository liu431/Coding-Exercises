# Solution 1: hash table to count items
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
        

# Soultion 2: use set to determine whether there are duplicate elements
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        
        
