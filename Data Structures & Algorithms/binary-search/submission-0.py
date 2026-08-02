class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            s=(l+r)//2
            if nums[s]==target:
                return s
            elif nums[s]<target:
                l=s+1
            elif nums[s]>target:
                r=s-1
        return -1


