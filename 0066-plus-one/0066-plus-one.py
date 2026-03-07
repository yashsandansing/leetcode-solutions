class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits
        carry = 1
        for ind in range(len(digits) - 1, -1, -1):
            temp = digits[ind] + carry
            digits[ind] = temp % 10
            carry = temp // 10
            if carry == 0:
                break

        if carry == 1:
            return [1] + digits

        return digits