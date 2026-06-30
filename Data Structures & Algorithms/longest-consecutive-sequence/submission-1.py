class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        res=0
        a=0
        for n in nums:
            if n-1 not in numset:
                l=1
                while (n+1) in numset:
                    l+=1
                    n+=1
                res=max(res,l)
               
        return res        