class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        cheap_2 = sum(sorted(prices)[:2])
        if cheap_2 <= money:
            return money - cheap_2
        else:
            return money
        
# Time complexity: O(nlog⁡n)
# Space complexity: O(n)
