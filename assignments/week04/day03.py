def f(n):
  if n<0:
    print ('enter a positive n!')
    return
  if n==1:

    return 0
  elif n==2:

    return 1
  else:
    return (f(n-1)+f(n-2))


# driver
print(f(int(input('enter n: '))))