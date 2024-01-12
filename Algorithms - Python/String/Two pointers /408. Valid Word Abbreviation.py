import re

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        arr = re.compile(r'\D+|\d+').findall(abbr)
        print(arr)
        # check by comparing different chunks
        word_ind = 0
        abbr_ind = 0
        comp_len = 0
        for i in arr:
            if i[0] == '0' or i == '0':
                return False
            try:
                comp_len = int(i)
                word_ind += comp_len
                abbr_ind += len(i)
                if word_ind > len(word):
                    return False
            except:
                comp_len = len(i)
                if word[word_ind: word_ind + comp_len] != abbr[abbr_ind: abbr_ind + comp_len]:
                    return False
                word_ind += len(i)   
                abbr_ind += len(i)                

        return word_ind == len(word)
