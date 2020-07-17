# https://leetcode.com/problems/fizz-buzz/
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # arr = ["1", "2"]
        # if n==1:
        #     arr = ["1"]
        # if n==2:
        #     arr = ["1", "2"]
        # elif(n>2):
        #     for i in range (3, n+1):
        #         if (i%3 == 0 and i%5 == 0) :
        #             arr.append('FizzBuzz')
        #         elif i%3 ==0:
        #             arr.append("Fizz")
        #         elif (i%5 == 0):
        #             arr.append("Buzz")
        #         else:
        #             arr.append(str(i))
        # return arr       
        return ["Fizz" * ( not i % 3) + "Buzz" * (not i % 5) or str(i) for i in range(1,n+1)]

##################################################


#  https://leetcode.com/problems/reverse-integer
# a = abs(123)
# d = 0
# while(a > 0):
#   c = a%10
#   a = a//10
#   d = d*10 + c 
# print(d)

class Solution:
    def reverse(self, x: int) -> int:
    
        rev = int(str(abs(x))[::-1])
        if rev.bit_length() < 32:
            return (-rev if x < 0 else rev)       
        else:
            return 0


############################################################

# . Given a string print all the vovels present in i
def CheckVow(string):
  final = []
  for xchar in string:
   if xchar in 'aeiou':
      final.append(xchar)      
  print(final)
  print(len(final))     
# Driver Code 
string = "the quick brown fox jumped over the lazy old dog"

# a = input('enter string')
CheckVow(string); 

################################################################

# Given a string apple banana sum check for space present in it

string = 'apple banana sum'
if ' ' in string: print ('space present')
else: print('space not present')