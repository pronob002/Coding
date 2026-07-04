class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash={}
        l=0
        res=0
        for r in range(len(s)):
            hash[s[r]]=1+hash.get(s[r],0)
            length=r-l+1
            while length-max(hash.values())>k:
                hash[s[l]]-=1
                l+=1
                length=r-l+1
                
            res=max(res,length)
        return res