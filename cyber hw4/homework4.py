import os
import math
import hashlib

#global vars
pw_and_freq = {}
prob_list = []

def Q1A():
	
	pw_file = open("../../pwds300", "r")
	
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

	for pw in sorted(pw_and_freq):
		#format output.
		result_file.write("{}\t{}\t{:.10f}\n".format(pw,pw_and_freq[pw],pw_prob(pw_and_freq[pw])))
		
	pw_file.close()
	result_file.close()
	#print(len(pw_and_freq))
	
#calculate probability	
def pw_prob(pw_freq):
	probability = round(float(pw_freq)/320412510.0,10)
	prob_list.append(float(probability))
	return float(probability)

def Q2A():
	#entropy = sum of probablity*log(probability) for each password.
	#for each prob in problist, calculate entropy and then add 'em all up.
	result_file = open('Q2A.txt','w+')
	entropy = 0.0
	for prob in prob_list:
		entropy += -prob*math.log(prob,2)
	#print "%.3f" %(entropy)
	result_file.write("%.3f" %(entropy))
	result_file.close()

def Q2B():
	#max entropy = log2(number of unique pw).
	#In this case, number of unique passwords = length of dictionary. 
	max_entropy = math.log(len(pw_and_freq),2)
	result_file = open('Q2B.txt','w+')
	result_file.write("%f" %(max_entropy))
	result_file.close()

#repeat Q2A but this time, only unique passwords(multiset from the pws file) out of the first column from pw_and_freq
# num of unique pws = length of dictionary.
def Q3A():
	result_file = open('Q3A.txt','w+')
	entropy = 0.0
	num_of_unique_pw = float(len(prob_list))
	print num_of_unique_pw
	for i in range(len(prob_list)):
		probability = (1.0/num_of_unique_pw)
		print "probability: %.10f" %(probability)
		entropy += -probability*math.log(probability,2)
	print "%.3f" %(entropy)
	result_file.write("%.3f" %(entropy))
	result_file.close()

#Q3B : the answer for Q3A is the same as the max entropy from Q2B. 

#brute force search for password, given hash values. Dictionary is sorted by pws(order of likelyhood), so it would take less than O(n), hopefully.
def Q4():
	md5_val = []
	in_file = open('Q4in.text')
	for line in in_file:
		md5_val.append(line.strip())
	in_file.close()
	result_file = open('Q4.txt','w+')
	
	##this loop will run in O(n) because it's iterating the whole dictionary of size n, and comparison(if) takes a constant time, so total of O(n).##
	##if we find all four pws before O(n), it will run for i iterations, but in the worst case, it will run for O(n).
	i = 1; #keep index
	count = 0 #keep counting until all four md5's have been found.
	
	for pw in pw_and_freq:
		#hash password and see if it matches one of the four from md5's
		hashed_val = (hashlib.md5(pw)).hexdigest()
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
			print "stopped at ith iteration!"
			return
		i+=1
	result_file.close()

def main():
	Q1A()
	Q2A()
	Q2B()
	Q3A()
	Q4()

main()
