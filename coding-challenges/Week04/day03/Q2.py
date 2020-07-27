def subString(word,n):

	#is to pick the starting point of the string
	for a in range (1,n+1):

		#is to pick the ending point of the string
		for i in range(n-a+1):
			#print the letters from the current starting point to the current ending point
			j=i+a-1
			
			#to print the string
			for x in range(i,j+1):
				print(word[x],end="")
			print()

#https://www.geeksforgeeks.org/program-print-substrings-given-string/

word="abcd"
length=len(word)
subString(word,length)