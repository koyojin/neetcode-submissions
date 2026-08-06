class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pin=0
        for i in range(len(matrix)):
            if matrix[i][0]<=target and matrix[i][len(matrix[i])-1]>=target:
                pin=i
                break

        l,r = 0, len(matrix[pin])-1
        while l<=r:
            mid = (l+r)//2
            if matrix[pin][mid]==target:
                return True
            elif matrix[pin][mid]<target:
                l=mid+1
            else:
                r=mid-1
        return False