class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize the output list
        res = [[]]
        # Append the new element to all elements in current list
        for i in nums:
            res += [curr + [i] for curr in res]
        return res
        
