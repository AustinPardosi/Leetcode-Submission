class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert2Minutes(time: str) -> int:
            hour, minute = time.split(":")
            return int(hour)*60 + int(minute)
        
        sortedMinutes = []
        for time in timePoints:
            converted = convert2Minutes(time)
            sortedMinutes.append(converted)
        sortedMinutes = sorted(sortedMinutes)

        minDiff = sortedMinutes[0] + 1440 - sortedMinutes[-1]
        for i in range(1, len(sortedMinutes)):
            diff = sortedMinutes[i] - sortedMinutes[i-1]
            minDiff = min(diff, minDiff)
        return minDiff