class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=[[p,q] for p,q in zip(position,speed)]
        stack=[]
        for p,s in sorted(car)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)