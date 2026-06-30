class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if i.isalnum():
                res+=i.lower()
        r=""
        for s in range(len(res)-1,-1,-1):
            r+=res[s]
        if r==res:
            return True
        else:
            return False
        