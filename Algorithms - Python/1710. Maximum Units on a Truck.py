class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort the box types with the number of units per box non-increasingly.
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        output = 0
        remainingSize = truckSize
        # box[0]: Number of boxes of that type
        # box[1]: Number of units inside each box of that type
        # Greedy approach: iteratively fill the truck by picking up the boxes having maximum units from the remaining boxes at every point
        for box in boxTypes:
            # Take all boxes of that type
            if box[0] <= remainingSize:
                output += box[0] * box[1]
                remainingSize -= box[0]
            # Take some boxes of that type to fill the space
            else:
                output += remainingSize * box[1]
                remainingSize = 0 
                break
        return output
                
            
        
