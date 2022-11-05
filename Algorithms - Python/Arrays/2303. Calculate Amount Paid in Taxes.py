class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        b_gap = [brackets[0]]
        for i in range(1, len(brackets)):
            gap = brackets[i][0] - brackets[i - 1][0]
            b_gap.append([gap, brackets[i][1]])
        
        tax = 0
        remain = income
        for g in b_gap:
            paid = min(g[0], remain)
            tax += paid * g[1] * 0.01
            remain -= paid
            if remain == 0:
                return tax
