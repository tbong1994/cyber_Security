
def evenOrOdd(num1):
	if(num1%2 or num1==0):
		print "even"
	else:
		print "odd"
		
def sumNum(num1,num2):
	try:
		number1 = int(num1)
		number2 = int(num2)
	except ValueError:
		print "Input must be integers"
	
	else:
		print num1 + num2

#sumNum(5,6)
#sumNum("hi",4) #this returns the error message.

def numberOfEven(list):
	count = 0
	if(len(list)==0):
		print "list empty"
	#also need to check if list contains only integers.
	else:
		for num in list:
			try:
				number = int(num)
			except ValueError:
				print "list must contain integers only!"
				return
			else:
				if(num%2==0 or num==0):
					count += 1
	print count
	
#l1 = [4,2,5,"what",7,8,2,"hey",15,23]			
#numberOfEven(l1)

#fix this.
def palindrome(word):
	try:
		check = str(word)
	except:
		print "input must be a string"
	else:
		for i in range((len(word))/2):
			if(word[i]==word[-i-1]):
				continue
			else:
				print false
				return	

#palindrome("abcdefedcba")

#dictionary definition.
d = {3:'a',4:'b'}

#accessing dictionary => dictionaryName[key]
#then keyvalue will be returned.
print d[3]
	
