# ACCEPTED

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        if len(rectangles) <= 2: return False

        numberRect = len(rectangles)
        x_intervals = [(x[0], x[2]) for x in rectangles]
        y_intervals = [(x[1], x[3]) for x in rectangles]

        x_intervals.sort()
        y_intervals.sort()

        mergedX = []
        mergedY = []

        for v1, v2 in x_intervals:
            if not mergedX or mergedX[-1][1] <= v1:
                mergedX.append([v1, v2])
            else:
                mergedX[-1][1] = max(mergedX[-1][1], v2)

        
        for v1, v2 in y_intervals:
            if not mergedY or mergedY[-1][1] <= v1:
                mergedY.append([v1, v2])
            else:
                mergedY[-1][1] = max(mergedY[-1][1], v2)

        return len(mergedX) > 2 or len(mergedY) > 2