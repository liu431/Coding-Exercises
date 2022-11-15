# Method 1: use extra list as a buffer
## Time complexity : O(n^2)
## Space complexity : O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        track = []
        for n in nums:
            if n in track:
                track.remove(n)
            else:
                track.append(n)
        return track[0]
      
# Method 2: use math
## 2∗(a+b+c)−(a+a+b+b+c)=c
## Time complexity : O(n)
## Space complexity : O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
      
 # Method 3: Bit Manipulation
## Time complexity : O(n)
## Space complexity : O(1)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
