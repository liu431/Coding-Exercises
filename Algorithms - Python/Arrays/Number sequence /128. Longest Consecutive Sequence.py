class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge case for empty input
        if not nums:
            return 0
        nums = sorted(set(nums))
        longest_seq = 1
        current_seq = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    # keep advancing the array
                    current_seq += 1
                else:
                    # stop and update record
                    longest_seq = max(longest_seq, current_seq)
                    current_seq = 1

        return max(longest_seq, current_seq)
