'''
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two
time-points in the list.
'''


class Solution:
    def findMinDifference(self, timePoints):
        def timeToMinutes(time):
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes
        minutesList = [timeToMinutes(time) for time in timePoints]
        minutesList.sort()
        minDiff = float('inf')
        for i in range(1, len(minutesList)):
            minDiff = min(minDiff, minutesList[i] - minutesList[i - 1])
        circularDiff = (24 * 60) - (minutesList[-1] - minutesList[0])
        minDiff = min(minDiff, circularDiff)

        return minDiff


timePoints = ["23:59","00:00"]
print(Solution().findMinDifference(timePoints))