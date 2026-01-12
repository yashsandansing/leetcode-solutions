class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highest, lowest = max(piles), 1
        bestEatingRate = highest

        while highest>=lowest:
            currEatingRate = (highest + lowest) // 2
            
            timeToEat = 0
            for pile in piles:
                timeToEat += (pile//currEatingRate) + (pile%currEatingRate > 0)
            
            if timeToEat > h:
                lowest = currEatingRate + 1
            else:
                highest = currEatingRate - 1
                bestEatingRate = currEatingRate

        return bestEatingRate