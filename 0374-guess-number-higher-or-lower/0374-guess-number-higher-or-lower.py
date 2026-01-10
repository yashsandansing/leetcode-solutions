# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lowest, highest = 1, n
        while lowest<=highest:
            middle = (highest + lowest)//2
            pred = guess(middle)
            if pred == -1:
                highest = middle - 1
            elif pred == 1:
                lowest = middle + 1
            else:
                return middle
        raise ValueError('Shouldnt be here bro')