class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records = []
        for i in ops:
            if i == 'C':
                records.pop()
            elif i == 'D':
                records.append(records[-1] * 2)
            elif i == '+':
                records.append(sum(records[-2:]))
            else:
                records.append(int(i))
        return sum(records)
