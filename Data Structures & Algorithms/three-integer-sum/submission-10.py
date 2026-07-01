class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        s=sorted(nums)
        for i in range(len(s)-1):
            if i>0 and s[i]==s[i-1]:
                continue
            a=s[i]
            t=-a
            L=i+1
            R=len(s)-1
            while(L<R):
                add=s[L]+s[R]
                if add > t:
                    R-=1
                elif add <t:
                    L+=1
                elif add==t:
                    res.append([a,s[L],s[R]])
                    L+=1
                    while s[L]==s[L-1] and L<R:
                        L+=1
        return res