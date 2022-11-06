class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # when two strings are the same
        if s1 == s2:
            return True
        # create index:letter map from s1
        s_dic = {i:letter for i, letter in enumerate(s1)}
        # keep only the unmatched pairs
        for i2, l2 in enumerate(s2):
            if s_dic[i2] == l2:
                s_dic.pop(i2, None)
            else:
                s_dic[i2] += l2
        # check if the unmatched pairs can be swapped
        if len(s_dic) == 2:
            print(s_dic)
            pairs = [value for key, value in s_dic.items()]
            if pairs[0] == pairs[-1][::-1]:
                return True
        return False
