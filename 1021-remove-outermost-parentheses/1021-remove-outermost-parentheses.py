class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a=[]
        b=0
        for c in s:
            if c=="(":
                if b>0:
                    a.append(c)
                b+=1
            elif c==")":
                b-=1
                if b>0:
                    a.append(c)
                    
           
                             
        return "".join(a)