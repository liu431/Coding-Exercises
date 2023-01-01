class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        mapped_word = set()
        s_list = s.split(" ")
        # return False when lengths are different
        if len(pattern) != len(s_list):
            return False
        # compare the patterns by matching
        for i, p in enumerate(pattern):
            word_in_s = s_list[i]
            if p not in mapping:
                if word_in_s in mapped_word:
                    return False
                else:
                    mapping[p] = word_in_s
                    mapped_word.add(word_in_s)
            else:
                if mapping[p] != word_in_s:
                    return False
        return True
