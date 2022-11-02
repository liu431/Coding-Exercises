class Solution:
    def reverseVowels(self, s: str) -> str:
        is_vowel = []
        vowel_list = []
        for i in s:
            if i.lower() in ['a', 'e', 'i', 'o', 'u']:
                is_vowel.append(True)
                vowel_list.append(i)
            else:
                is_vowel.append(False)
                
        new_s = ''
        for ind, flag in enumerate(is_vowel):
            if flag:
                new_s += vowel_list.pop()
            else:
                new_s += s[ind]
                
        return new_s
