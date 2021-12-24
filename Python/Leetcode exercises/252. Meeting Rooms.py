# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
## Sort all meetinsg by the start times
## The end time of the previous meeting should be smaller or equal to the start time of the next meeting
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sortedtime = sorted(intervals, key=lambda x: x[0])
        for i in range(len(sortedtime) - 1):
            if sortedtime[i][1] > sortedtime[i+1][0]:
                return False
        return True
        
        
