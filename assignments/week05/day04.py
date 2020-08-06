def generateParenthesis(n):
    op = []
    def pg(s,l,r):
        
        if (len(s) == 2*n):
            op.append(s)
            return
        
        if (l < n):
            pg(s+'(', l+1, r)
        if (r < l):
            pg(s+')', l, r+1)
      
    pg('', 0, 0)
    return op
    
print (generateParenthesis(3))