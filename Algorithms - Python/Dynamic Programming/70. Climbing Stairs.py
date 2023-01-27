class Solution:
    def climbStairs(self, n: int) -> int:
        # recursive approach (Time Limit Exceeded O(n))
        # def dp(n):
        #     if n <= 1:
        #         return 1
        #     else:
        #         return dp(n - 1) + dp(n -2)
        
        # return dp(n)
    
        # iterative approach 
        prev_2, prev_1 = 1, 1
        for i in range(n):
            prev_2, prev_1 = prev_1, prev_1 + prev_2
        return prev_2
