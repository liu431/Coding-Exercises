class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort the array in descending order
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)-2):
            # test whether the current 3 largest values would form a triangle
            c = nums[i]
            b = nums[i+1]
            a = nums[i+2]
            # The sum of two smaller sides should be larger than the largest side
            if c - b < a:
                # Return perimeter if the values work
                return c + b + a
        return 0
