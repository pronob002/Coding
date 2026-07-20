class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def backtrack(openN,endN):
            if openN==endN==n:
                res.append("".join(stack))
            if openN<n:
                stack.append("(")
                backtrack(openN+1,endN)
                stack.pop()
            if endN<openN:
                stack.append(")")
                backtrack(openN,endN+1)
                stack.pop()
        backtrack(0,0)
        return res
    
