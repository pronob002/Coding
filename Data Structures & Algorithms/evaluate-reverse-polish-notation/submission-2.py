class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=[]
        import operator
        sign={
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/':lambda a,b:int(a/b),
        }
        for i in tokens:

            if i == '+' or i== '-' or i=='*' or i== '/':
                a=res[-1]#5,2
                res.pop()
                b=res[-1]#13,4
                res.pop()
                res.append(sign[i](b,a))#2,6
            else:
                res.append(int(i))
        return res[0]