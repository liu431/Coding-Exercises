# Method 1: hash map
# Link: https://leetcode.com/problems/two-sum/solutions/127810/two-sum/
# A hash table is well suited for this purpose because it supports fast lookup in near constant time. I say "near" because if a collision occurred, a lookup could degenerate to O(n)O(n)O(n) time. However, lookup in a hash table should be amortized O(1) time as long as the hash function was chosen carefully.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store key: target - num; value: index of searched value
        pair = {}
        for ind, num in enumerate(nums):
            # Not find the match
            if num not in pair:
                pair[target - num] = ind
            # Find the match
            else:
                return [pair[num], ind]

# Complexity Analysis

# Time complexity: O(n). We traverse the list containing nnn elements only once. Each lookup in the table costs only O(1) time.

# Space complexity: O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nnn elements.

## Simplier code:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pair = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: 
                return [pair[r], i]
            pair[j] = i
		
