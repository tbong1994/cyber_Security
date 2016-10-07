import math
import hashlib

#global vars
pw_and_freq = {}
prob_list = []

def Q1A():
	
	pw_file = open("pwds300", "r")
	
	#output file
	result_file = open("Q1A.text","w+")
		
	#map passwords to number of occurences of the pws in the file.
	for pw in pw_file:
		#get rid of white space.
		st = pw.strip()
		#if password already exists in dictionary, increment value
		if(pw_and_freq.has_key(st)):
			pw_and_freq[st] += 1
		#if pw doesn't exist, then add it to dictionary.
		else:
			pw_and_freq[st] = 1
	#sort by passwords.
	sorted(pw_and_freq)
	
	for pw in pw_and_freq:
		#format output.
		result_file.write("%s\t%d\t%.10f\n" %(pw,pw_and_freq[pw],pw_prob(pw_and_freq[pw])))
		
	pw_file.close()
	result_file.close()
	print(len(pw_and_freq))
	
#calculate probability	
def pw_prob(pw_freq):
	probability = round(float(pw_freq)/320412510.0,10)
	return probability
	
Q1A()

def Q2A():
	#entropy = sum of probablity*log(probability) for each password.
	#for each prob in problist, calculate entropy and then add 'em all up.
	entropy = 0.0
	for prob in prob_list:
		entropy += -prob*math.log10(prob)
	result_file = open('Q2A.txt','w+')
	result_file.write("%f" %(round(entropy,3)))
	result_file.close()
	
#Q2A()

def Q2B():
	#max entropy = log2(number of unique pw).
	#In this case, number of unique passwords = length of dictionary. 
	max_entropy = 0.0
	max_entropy = math.log(len(pw_and_freq),2)
	result_file = open('Q2B.txt','w+')
	result_file.write("%f" %(max_entropy))
	result_file.close()

#def Q3A():
#repeat Q2A but this time, only unique passwords(multiset from the pws file) out of the first column from pw_and_freq
# num of unique pws = length of dictionary.

#def Q3B():
#samething as Q2B

#brute force search for password, given hash values. Dictionary is sorted by pws(order of likelyhood), so it would take less than O(n), hopefully.
def Q4():
	md5_val = ['ba931c15ec0163c4bb339f41571694ce','c9cd905fc459e5550b8c3b01d4346c25','e9269d9e52a692f52caece9d0e7cdae1','660719b4a7591769583a7c8d20c6dfa4']
	result_file = open('Q4.txt','w+')
	
	##this loop will run in O(n) because it's iterating the whole dictionary of size n, and comparison(if) takes a constant time, so total of O(n).##
	##if we find all four pws before O(n), it will run for i iterations, but in the worst case, it will run for O(n).
	i = 1; #keep index
	count = 0 #keep counting until all four md5's have been found.
	
	for pw in pw_and_freq:
		#hash password and see if it matches one of the four from md5's
		hashed_val = (hash.md5(pw)).hexdigest()
		if(hashed_val == md5_val[0]):
			#output format: md5		password	index in dictionary.
			result_file.write("%s\t%s\t%d\n" %(md5_val[0],pw,i))
			count += 1
		elif(hashed_val == md5_val[1]):
			result_file.write("%s\t%s\t%d\n" %(md5_val[1],pw,i))
			count += 1
		elif(hashed_val == md5_val[2]):
			result_file.write("%s\t%s\t%d\n" %(md5_val[2],pw,i))
			count += 1
		elif(hashed_val == md5_val[3]):
			result_file.write("%s\t%s\t%d\n" %(md5_val[3],pw,i))
			count += 1
		##if all four were found, then exit this loop.
		if(count == 4):
			return
		i+=1
	result_file.close()
#Q4()






	
def Practice():
	d = {'a':1,'b':1,'c':1,'d':1,'e':1,}
	result_file = open('practice.txt','w+')
	for elem in d:
		result_file.write("%s\t%d\n" %(elem, d[elem]))	
	result_file.close()
#Practice()


