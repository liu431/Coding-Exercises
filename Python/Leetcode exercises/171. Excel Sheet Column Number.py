class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        out = 0
        lens = len(columnTitle)
        if lens == 1:
            # Convert letter to value
            return ord(columnTitle) - 64
        else:
            for ind, letter in enumerate(columnTitle):
                # Calculate values based on their index and values
                out += (ord(letter) - 64) * (26 ** (len(columnTitle)-ind-1))
            return out
