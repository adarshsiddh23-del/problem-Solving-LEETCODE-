class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkins[id]

        travelTime = t - startTime

        route = (startStation, stationName)

        if route not in self.routes:
            self.routes[route] = [0, 0]

        self.routes[route][0] += travelTime
        self.routes[route][1] += 1

        del self.checkins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, count = self.routes[(startStation, endStation)]

        return totalTime / count