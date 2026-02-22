class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        best = num
        n = len(num_str)
        for i in range(n):
            for j in range(i+1, n):
                if num_str[j] > num_str[i]:
                    temp = num_str[:i] + num_str[j] + num_str[i+1:j] + num_str[i] + num_str[j+1:]
                    best = max(best, int(temp))
        return best