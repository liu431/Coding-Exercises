class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:

        while True:
            prev_arr = deepcopy(arr)
            for i in range(1, len(arr) - 1):
                val = prev_arr[i]
                #If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
                #If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
                arr[i] -= (val > prev_arr[i - 1] and val > prev_arr[i + 1])
                arr[i] += (val < prev_arr[i - 1] and val < prev_arr[i + 1])
            if prev_arr == arr:
                return arr
        
