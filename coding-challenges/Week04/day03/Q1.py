class Solution:
    def uniquePaths(self, m:int, n:int)-> int:
        pathDict={}
        return self.lookPath(m,n,pathDict)
    
    def lookPath(self,m,n,pathDict):
        if(m,n) in pathDict:
            return pathDict[(m,n)]
        elif m==1 or n==1:
            return 1
        
        pathDict[(m,n)]=self.lookPath(m-1,n,pathDict)+self.lookPath(m,n-1,pathDict)
        return pathDict[(m,n)]


#using formula C(m+n-2,n-1)
# import math
# def uniquePaths(m:int, n:int):
#         if not m or not n:
#             return 0
#         return int (math.factorial(m+n-2)/(math.factorial(n-1) * math.factorial(m-1)))
        
        

m=3
n=2
print(uniquePaths(m,n))