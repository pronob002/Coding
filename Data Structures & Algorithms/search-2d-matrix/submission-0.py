class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:



        def search(arr : List[int],target):
            l=0
            r=len(arr)-1
            while (l<=r):
                s=(l+r)//2
                if arr[s]==target:
                    return True
                elif arr[s]<target:
                    l=s+1
                else:
                    r=s-1
        for i in matrix:
            if search(i,target):
                return True
        return False
            
        