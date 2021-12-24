# Sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order
## First, create a dict to count the frequency of each value.
## Second, use lambda function to sort the list
## Use -x as the second key to sort values with same frequency in decreasing order
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cts = dict()
        for i in nums:
            cts[i] = cts.get(i, 0) + 1
        return sorted(nums, key = lambda x: (cts[x], -x))
        
