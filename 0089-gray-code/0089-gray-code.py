class Solution:
    def grayCode(self, n: int) -> List[int]:
        size = 1 << n
        res = []
        for i in range(size):
            res.append(i ^ (i >> 1))
            # print(i, res)
        return res