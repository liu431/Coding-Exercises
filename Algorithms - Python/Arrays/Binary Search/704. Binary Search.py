class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(start, end):
            if target < nums[0] or target > nums[-1]:
                return -1
            if start + 1 < end:
                mid = (start + end) // 2
                print(start, end, mid, nums[mid], target)
                if nums[mid] < target:
                    return binary(mid, end)
                elif nums[mid] > target:
                    return binary(start, mid)
                else:
                    return mid
            else:
                if target == nums[start]:
                    return start
                elif target == nums[end]:
                    return end
                else:
                    return -1
        return binary(0, len(nums))
