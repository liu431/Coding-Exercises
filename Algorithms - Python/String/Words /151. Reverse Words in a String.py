class Solution:
    def reverseWords(self, s: str) -> str:
        word = [i.strip() for i in s.split(' ') if i]
        return ' '.join(word[::-1])
