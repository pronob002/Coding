class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R=0,len(numbers)-1
        while (L<R):
            add=numbers[L]+numbers[R]
            if add>target:
                R-=1
            if add<target:
                L+=1
            if add==target:
                return [L+1,R+1] 
