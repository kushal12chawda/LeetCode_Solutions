class Solution(object):
    def findMinDifference(self, timePoints):
        timePoints.sort()
        min_diff = float('inf')
        
        for i in range(len(timePoints)):
            t1 = self.toMinutes(timePoints[i])
            t2 = self.toMinutes(timePoints[(i + 1) % len(timePoints)])
            min_diff = min(min_diff, (t2 - t1) % (24 * 60))  
        
        return min_diff

    def toMinutes(self, time):
        h, m = map(int, time.split(":"))
        return h * 60 + m