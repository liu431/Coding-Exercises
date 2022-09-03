class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # Initialize the result list
        res = []
        # Edge case when nums is null
        if len(nums) == 0:
            if upper == lower:
                res.append(str(lower))
            else:    
                res.append(str(lower)+'->'+str(upper))
            return res
        
        # Far left: when lower is smaller than first num
        if nums[0] > lower:
            if lower == nums[0] - 1:
                res.append(str(lower))
            else:
                res.append(str(lower)+'->'+str(nums[0]-1))
        
        # Middle: add the smallest sorted list of ranges
        for i in range(len(nums) - 1):
            if nums[i] >= lower and nums[i+1] <= upper:
                if nums[i+1] - nums[i] == 2:
                    res.append(str(nums[i] +1))
                if nums[i+1] - nums[i] > 2:
                    res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        
        # Far right: when upper is larger than the last num 
        if nums[-1] < upper:
            if upper == nums[-1] + 1:
                res.append(str(upper))
            else:
                res.append(str(nums[-1]+1)+'->'+str(upper))
        return res
            
        
