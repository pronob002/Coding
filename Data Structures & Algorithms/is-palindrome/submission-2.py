class Solution:
    def isPalindrome(self, s: str) -> bool:
        L=0
        R=len(s)-1
        while L<R:
            while L<R and not (self.alpha(s[L])):
                L+=1
            while L<R and not (self.alpha(s[R])):
                R-=1
            if s[L].lower()!=s[R].lower():
                return False
            L+=1
            R-=1
        return True
    def alpha(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or 
            ord('a')<=ord(c)<=ord('z') or
            ord('0')<=ord(c)<=ord('9'))