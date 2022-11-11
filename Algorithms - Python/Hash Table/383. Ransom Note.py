class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Construct dict for letters in magazine
        letter_dic = {x : magazine.count(x) for x in set(magazine)}
        # Or: letter_dic = collections.Counter(magazine)
        for i in ransomNote:
            # Letter that is in magazine
            if i in letter_dic:
                l_ct = letter_dic[i]
                # Reduce count by 1
                if l_ct > 0:
                    letter_dic[i] -= 1
                # Count 0 -> False
                else:
                    return False
            # Letter that is not in magazine
            else:
                return False
        return True

    

class Solution:
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    letters = collections.Counter(magazine)
    for i in ransomNote:
        if letters[i] <= 0:
            return False
        else:
            letters[i] -= 1
    return True
