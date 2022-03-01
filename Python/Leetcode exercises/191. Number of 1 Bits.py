class Solution:
    def hammingWeight(self, n: int) -> int:
        # Takes an unsigned integer and counts the number of '1' bits it has
        return bin(n).count('1')
        
