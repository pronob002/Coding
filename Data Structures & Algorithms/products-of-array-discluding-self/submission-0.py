class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_nums=[1]+nums+[1]
        res=[]
        pre=1
        post=1
        for i in range(1,len(nums)+1):
            pre=pre*new_nums[i-1]
            res.append(pre)
        for j in range(len(nums),0,-1):
            post=post*new_nums[j+1]
            res[j-1]=res[j-1]*post
        return res
        