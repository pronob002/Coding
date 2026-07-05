class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=[0]*26
        win=[0]*26
        if len(s1)>len(s2):
            return False
        for i in s1:
            need[ord(i)-ord('a')]+=1
        for j in s2[:len(s1)]:
            win[ord(j)-ord('a')]+=1
        if need==win:
            return True
        l=0
        for r in range(len(s1),len(s2)):
            win[ord(s2[r])-ord('a')]+=1
            win[ord(s2[r-len(s1)])-ord('a')]-=1
            if need==win:
                return True
        return False
