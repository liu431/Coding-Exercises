class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Define function to format output strings
        def res_format(sub, res):
            if len(sub) == 1:
                res.append(str(sub[0]))
            else:
                res.append(str(sub[0]) + '->' + str(sub[-1]))  
        # Edge case when input array is empty
        if nums == []:
            return nums
        
        res = []
        sub = [nums[0]]
        # At each step, take actions based on whether next number is incremendal
        for i in range(len(nums) -1):
            if nums[i] + 1 == nums[i + 1]:
                sub.append(nums[i + 1])
            else:
                res_format(sub, res)
                sub = [nums[i + 1]]
        # Put the last range into the result list
        res_format(sub, res)
        return res
                
                
                
            
        
