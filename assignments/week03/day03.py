n = int(input('enter no of participants: '))

s = sorted(list(set(map(int, input('enter the scores seperated by space: ').split()[:n]))))

print(s[len(s)-2])