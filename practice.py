import operator

def num_compare():
	num1 = int(raw_input("enter a number "))
	num2 = int(raw_input("enter a number again"))
	
	if(num1 == num2):
		print "same"
	elif(num1>num2):
		print "first number %d is greater" %(num1)
	else:
		print "second number %d is greater" %(num2)
		
#num_compare()

def palindrome(n):
	#pal = str(raw_input("enter a string")
	#return pal == pal[::-1]
	for word in n:
		if(word == word[::-1]): #palindrome logic for python.
			print "palindrome"
		else:
			print "not a palin"
l1 = ["abcdcba","abcdcbe","abcdefedcba","abcasdfxccba",]
palindrome(l1)
