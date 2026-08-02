class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot=0,len(matrix)-1
        while top<=bot:
            row=(top+bot)//2
            if target>matrix[row][-1]:
                top=top+1
            elif target<matrix[row][0]:
                bot=bot-1
            else:
                break
        if not top<=bot:
            return False
        row=(top+bot)//2
        l,r=0,len(matrix[0])-1
        while l<=r:
            s=(l+r)//2
            if matrix[row][s]==target:
                return True
            elif matrix[row][s]<target:
                l=l+1
            elif matrix[row][s]>target:
                r=r-1
        return False

            
        