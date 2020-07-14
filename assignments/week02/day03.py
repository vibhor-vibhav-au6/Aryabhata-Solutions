#Prime Number or not
for i in range(2, n):
  if (n%i == 0):
    print('not prime')
    break
else:
  print('prime')

#########################################

def pattern(n):
  for row in range(1,n+1):
    for col in range(1, row+1):
      print(col, end = " ")
    print()
    # or use the following code snippet
    # [print (col, end =' ') for col in range(1, row+1)]
    # print()