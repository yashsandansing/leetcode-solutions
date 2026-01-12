class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowest, highest = 0, 0
        for w in weights:
            lowest = max(lowest, w)
            highest+=w
        
        best_capacity = highest

        while lowest<=highest:
            curr_capacity = (lowest + highest) // 2
            
            curr_days = 0
            curr_holding = 0
            for w in weights:
                if curr_holding + w >curr_capacity:
                    curr_days+=1
                    curr_holding = w
                else:
                    curr_holding += w
            
            if curr_holding > 0:
                curr_days+=1
            
            if curr_days > days:
                lowest = curr_capacity + 1
            
            else:
                highest = curr_capacity - 1
                best_capacity = min(best_capacity, curr_capacity)
        
        return best_capacity