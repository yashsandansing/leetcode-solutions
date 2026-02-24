class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # at least one building
        # heights can be from 1 to really large
        # return list should be ordered -> from left to right

        # brute-force
        # l to right
        # i to i + 1
        # if any j exists that is greater than i, dont add i to list
        # if we are at end of the list and we havent encountered
        # any height add i to the list

        res = []
        n = len(heights)
        max_height = float('-inf')

        for h in range(n-1, -1, -1):
            if heights[h] <= max_height:
                continue
            else:
                max_height = heights[h]
                res.append(h)
        
        return res[::-1]