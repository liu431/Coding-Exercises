class UndergroundSystem:

    def __init__(self):        
        self.check = {}
        self.tripTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        print('in', id)
        self.check[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        print('out', id)
        checkInInfo = self.check.pop(id, None)
        checkInStation, checkInTime = checkInInfo[0], checkInInfo[1]
        stationPair = (checkInStation, stationName)
        tripTime = t - checkInTime
        if stationPair not in self.tripTimes:
            self.tripTimes[stationPair] = [tripTime]
        else:
            self.tripTimes[stationPair].append(tripTime)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        print('avg')
        allTimes = self.tripTimes[(startStation, endStation)]
        return sum(allTimes) / len(allTimes)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
