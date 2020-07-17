class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        numMap = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
              
        arr = [num1,num2]
        sumArr = []
        for i in arr:
            num = 0
            base = 10
            for char in i:
                num = num*base + numMap[char]
            sumArr.append(num)
        
        sum = sumArr[0]+ sumArr[1]
        return (str(sum))