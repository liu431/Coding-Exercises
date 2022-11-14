# Sol 1: reverse loop by comparing mapped value
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
        curr = roman[s[-1]]
        val = curr
        for char in s[:-1][::-1]:
            new_curr = roman[char]
            if new_curr < curr:
                val -= new_curr
            else:
                val += new_curr
            curr = new_curr
        return val
      
 # Sol 2: by custom logic
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total_val = 0
        for i, l in enumerate(s):
            val = mapping[l]
            if i != len(s) - 1:
                if l == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    val *= -1
                if l == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    val *= -1
                if l == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    val *= -1
            total_val += val
        return total_val
