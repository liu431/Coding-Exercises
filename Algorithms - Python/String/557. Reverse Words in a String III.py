class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([''.join(i[::-1]) for i in s.split(' ')])
