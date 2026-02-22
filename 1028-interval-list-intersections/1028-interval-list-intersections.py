class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # can any list be empty. if so what the ouput => empty
        # intevals cant be negative
        # intersection can be of unit len => 15, 24 | 24, 25 => 24, 24

        # [[0,2],[5,10],[13,23],[24,25]]
        # [[1,5],[8,12],[15,24],[25,26]]
        # [[1,2],[5,5], [8,10], [15,23],[24,24],[25,25]]

        # brute force = loop thru both 
        # if firstEnd <= secondStart or secondEnd <= firstStart => create an intersection continue
        # intersection = max(firstStart, secondStart), min(firstEnd, secondEnd)

        res = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            firstStart, firstEnd = firstList[i]
            secondStart, secondEnd = secondList[j]

            intersection = min(firstEnd, secondEnd) - max(firstStart, secondStart)
            if intersection >= 0:
                res.append([max(firstStart, secondStart), min(firstEnd, secondEnd)])

            # choose which i or j to update
            if firstEnd <= secondEnd:
                i += 1
            else:
                j += 1

        return res