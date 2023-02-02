class Solution:
    def checkRecord(self, s: str) -> bool:
        # # 'A' strictly fewer than 2 days
        # print(s.count('A'))
        # # no 'LLL' in self
        # print('LLL' in s)
        # return s.count('A') < 2 and 'LLL' not in s
        count_A = 0
        for ind, i in enumerate(s):
            if i == 'A':
                count_A += 1
            if i == 'L' and ind <= len(s) - 3:
                print('first L')
                if s[ind:ind+3] == 'LLL':
                    return False
        return count_A < 2
