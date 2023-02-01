class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums_set = set(nums)
        # nums_set_sorted = sorted(nums_set)
        # if len(nums_set) < 3:
        #     return nums_set_sorted[-1]
        # else:
        #     return nums_set_sorted[-3]
        #first, second, third = nums[0], nums[1], nums[2]

        nums = list(set(nums))
        max_nums = sorted(nums[:3])
        print(max_nums)
        if len(max_nums) < 3:
            return max_nums[-1]
        for i in nums[3:]:
            print(i)
            if i > max_nums[-1]:
                print('largest')
                max_nums = max_nums[1:] + [i]

            elif i > max_nums[1] and i < max_nums[2]:
                max_nums = [max_nums[1], i, max_nums[2]]
            elif i > max_nums[0] and i < max_nums[1]:
                max_nums = [max_nums[0], i, max_nums[1]]
            else:
                pass
        print(max_nums)
        return max_nums[0]               


O(n)
