n = int(input('enter n: '))
# n = 4

for i in range (1,n+1):
  for j in range (n-i,0,-1):
    print(' ', end='')
  for j in range(i):
    print('*', end =' ')
  
  print()

# or the soln below
 
for i in range(1,n+1):
  print("-" * (n - i), end = "")
  print("* " * i, end = "")
  print()



 