class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = int(len(s) / 2)
        s1 = s[:half]
        s2 = s[half:]

        def vowel_count(a):
            cts = 0
            for i in a.lower():
                if i in ('a', 'e', 'i', 'o', 'u'):
                    cts += 1
            return cts

        return vowel_count(s1) == vowel_count(s2)
