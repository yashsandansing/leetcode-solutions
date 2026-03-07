class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        max_num = "0"
        swap_i = swap_j = -1

        for n in range(len(num) - 1, -1, -1):
            if num[n] > max_num:
                max_num = num[n]
                max_ind = n
            
            if num[n] < max_num:
                swap_i, swap_j = n, max_ind

        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        
        return int("".join(num))