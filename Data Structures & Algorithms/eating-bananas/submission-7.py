import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=max(piles)
        while l<=r:
            m=(l+r)//2
            
            hr=0
            for i in piles:
                hr+=math.ceil(i/m)
            if hr<=h:
                res=m
                r=m-1
            elif hr>h:
                l=m+1
            
        return res