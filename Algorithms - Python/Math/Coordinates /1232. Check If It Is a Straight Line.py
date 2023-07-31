import math
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def getK(i):
            first_x, first_y = coordinates[i]
            second_x, second_y = coordinates[i + 1]
            if second_x == first_x:
                return math.inf
            elif second_y == first_y:
                return 0
            else:
                return (second_y - first_y) / (second_x - first_x)

        initial = getK(0)
        print(initial)    
        for i in range(1, len(coordinates) - 1):
            k = getK(i)
            if k != initial:
                return False
        
        return True

