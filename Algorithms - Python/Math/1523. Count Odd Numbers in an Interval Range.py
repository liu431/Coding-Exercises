class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low_is_odd = (low % 2 == 1)
        high_is_odd = (high % 2 == 1)
        if low_is_odd and high_is_odd:
            return 2 + (high - low - 1) // 2
        elif low_is_odd == False and high_is_odd == False:
            return (high - low) // 2
        else:
            return int((high - low + 1) / 2)
