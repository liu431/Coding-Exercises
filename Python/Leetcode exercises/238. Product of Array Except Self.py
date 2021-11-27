class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# Comment out as this algorithm exceeds time limit 
#        def product(num):
#            '''
#            Calculate product of input array; Return 1 when array is empty
#            '''
#            ans = 1
#            for i in num:
#                ans *= i
#            return ans
#        res = []
#        lens = len(nums)
        # Fill the result array with left array prefix product
        # res = [ for i in range(lens)]
        # Multiple right array suffix product
#        res = [product(nums[:i]) * product(nums[i+1:]) for i in range(lens)]
#        return res

        lens = len(nums)
        output = [1] * lens
        
        # multiply by the left side
        left_product = 1
        for i in range(1, lens):
            left_product *= nums[i-1]
            output[i] = left_product
        
        # multiply by the right side
        right_product = 1
        for i in range(lens-2, -1, -1):
            right_product *= nums[i+1]
            output[i] *= right_product
        
        return output
        
        
