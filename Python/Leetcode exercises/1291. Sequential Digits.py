# An integer has sequential digits if and only if each digit in the number is one more than the previous digit. Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
## Use list comprehension to generate sequential digits based on number of digits
## Add to the res if it is in the range and not contains 0
## Increment the iterator
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        output = []
        a = low
        while a <= high:
            seq = int(''.join([str(int(str(a)[0]) + i) for i in range(len(str(a)))]))
            if seq >= low and seq <= high and '0' not in str(seq):
                 output.append(seq)
            a += 10**(len(str(a))-1)
        return output
        
