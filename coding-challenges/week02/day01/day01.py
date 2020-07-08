# Write a program that takes input from the user as marks in 5 subjects and assigns a
# grade according to the following rules:
# Perc = (s1+s2+s3+s4+s5)/5.
# A, if Perc is 90 or more B, if Perc is between 70 and 90(not equal to 90) C, if Perc is
# between 50 and 70(not equal to 90) D, if Perc is between 30 and 50(not equal to 90) E,
# if Perc is less than 30




s1 = int(input('enter your marks in subject 1:'))
s2 = int(input('enter your marks in subject 2:'))
s3 = int(input('enter your marks in subject 3:'))
s4 = int(input('enter your marks in subject 4:'))
s5 = int(input('enter your marks in subject 5:'))

perc = (s1 + s2 + s3 + s4 + s5)/5

if ((s1 or s2 or s3 or s4 or s5) > 100):
    print('please enter valid marks!')
elif(perc >= 90):
    print('grade A')
elif(perc >= 70):
    print('grade B')
elif(perc >=50):
    print('grade C')
elif(perc >= 30):
    print('grade D')
else:
    print('grade E')





