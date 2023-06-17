class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # initialize two arrays to track the accumulative max and min
        lens = len(arr)
        left_max = [0] * lens
        right_min = [0] * lens
        left_max[0] = arr[0]
        right_min[-1] = arr[-1]

        # loop through the array to construct the two arrays
        for i in range(1, lens):
            print(i, arr[i], arr[i - 1])
            left_max[i] = max(arr[i], left_max[i - 1])
            i_r = lens - 1 - i
            right_min[i_r] = min(arr[i_r], right_min[i_r + 1])
        print(left_max, right_min) 

        # count possible partitions
        cts = 1
        for i in range(lens - 1):
            if left_max[i] <= right_min[i + 1]:
                cts += 1

        return cts
