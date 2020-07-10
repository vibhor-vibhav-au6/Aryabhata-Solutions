a = input('enter no 1')
b = input('enter no 2')
c = input('enter choice')

if c == '1':
  print(int(a)+ int(b))
elif c == '2':
  print(int(a) - int(b))
elif c == '3':
  print(int(a)* int(b))
elif c == '4':
  print(int(a) / int(b))
elif c != ('1' or '2' or '3' or '4'):
  print('enter a valid choice')

# ************************************************************************************

a = int(input('enter a no : '))

if (a%2 == 0):
  print('even')
else:
  print ('odd')

# or

if ((a//2)*2 == a):
  print('even')
else:
  print('odd')