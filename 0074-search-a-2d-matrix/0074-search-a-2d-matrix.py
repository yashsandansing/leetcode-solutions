class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        i = 0
        while l<=r:
            midCol = (l+r)//2
            if matrix[midCol][0]<=target<=matrix[midCol][-1]:
                break
            else:
                if target>matrix[midCol][-1]:
                    l = midCol+1
                else:
                    r = midCol-1
        l=0
        r = len(matrix[midCol])-1
        while l<=r:
            mid = (l+r)//2
            pred = matrix[midCol][mid]
            if target == pred:
                return True
            elif target<pred:
                r = mid-1
            else:
                l = mid+1
            
        return False



