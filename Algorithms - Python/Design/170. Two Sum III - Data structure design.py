class TwoSum(object):

    def __init__(self):
        self.arr = []

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.arr.append(number)
        

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        dic = {}
        for i in self.arr:
            if i not in dic:
                dic[value - i] = i
            else:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
