import os
import math
import hashlib


#global vars
pw_and_freq = {}  #password dictionary
prob_list = []  #array of probability for each unique pw
num_pwds = 0  #count # of pwds from the input file

def Q1A():
	pw_file = open("../../passwords-hw4", "r")
	#output file
	result_file = open("Q1A.text","w+")
	global num_pwds
	#map passwords to number of occurences of the pws in the file.
	for pw in pw_file:
		num_pwds += 1
		#get rid of white space.
		st = pw.strip()
		#if password already exists in dictionary, increment value
		if(pw_and_freq.has_key(st)):
			pw_and_freq[st] += 1
		#if pw doesn't exist, then add it to dictionary.
		else:
			pw_and_freq[st] = 1
	
	for pw in sorted(pw_and_freq.iterkeys()):
		#format output.
		result_file.write("{}\t{}\t{:.10f}\n".format(pw,pw_and_freq[pw],pw_prob(pw_and_freq[pw])))
		
	pw_file.close()
	result_file.close()
	#print(len(pw_and_freq))
	
#calculate probability	
def pw_prob(pw_freq):
	probability = round(float(pw_freq)/float(num_pwds),10)
	prob_list.append(float(probability))
	return float(probability)

def Q2A():
	#entropy = sum of probablity*log(probability) for each password.
	#for each prob in problist, calculate entropy and then add 'em all up.
	result_file = open('Q2A.txt','w+')
	entropy = 0.0
	for prob in prob_list:
		entropy += -prob*math.log(prob,2)
	result_file.write("%.3f" %(entropy))
	result_file.close()

def Q2B():
	#max entropy = log2(number of pw in the file, because for max entropy you assume that every element is unique, ie) only 1 occurence). 
	max_entropy = math.log(len(num_pwds),2)
	result_file = open('Q2B.txt','w+')
	result_file.write("%f" %(max_entropy))
	result_file.close()

##Q2C
##why maximum entropy is not achieved?

#repeat Q2A but this time, only unique passwords(multiset from the pws file) out of the first column from pw_and_freq
# num of unique pws = length of dictionary.
def Q3A():
	result_file = open('Q3A.txt','w+')
	entropy = 0.0
	num_of_unique_pw = float(len(prob_list))
	print num_of_unique_pw
	for i in range(len(prob_list)):
		probability = (1.0/num_of_unique_pw)
		entropy += -probability*math.log(probability,2)
	result_file.write("%.3f" %(entropy))
	result_file.close()

##Q3B
##the answer for Q3A is the same as the max entropy from Q2B. 

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
	
	count = 0 #keep counting until all four md5's have been found.
	
	#sorting dictionary by values (mydict.iteritems(), key=lambda (k,v): (v,k))...
	#reference from http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
	
	#iterate through the md5_val and for each value in md5_Val, compare that value with the hash value of the 
	#password from the sorted list. and return.
	for md5 in md5_val :
		i = 1 #keep rank
		for pw, freq in sorted(pw_and_freq.iteritems(), key=lambda (k,v):(v,k)):
			hashed_val = (hashlib.md5(pw)).hexdigest() #hash password to be compared with the hash val from the input file. 
			if(hashed_val == md5):
				#output format: md5		password	index in dictionary.
				result_file.write("%s\t%s\t%d\n" %(md5,pw,i))
				count += 1
				continue 
			##if all four were found, then exit this loop.
			if(count == len(md5_val)):
				#stop if all the md5 values are found in the dictionary.
				print "stopped at ith iteration!"
				return
			i+=1
	result_file.close()
##Q5)
##A)Lorenzo (name of player), football,BuffBills(shortname for Buffalo Bills), 
##B)Yes, because if I have the basic knowledge of what the pw may be, then I can neglect other irrelvent information.
###for example, I only need to look for last names of the players on Buffalo Bills team.
##C)This shrinks the range of guessing for me as it lets me know to look for the specific person who retired on April 7th of 2016. It will
##be easier than looking for everyone who had retired.
##D)With the side channel, you can go online and search for the hash value and find the corresponding password for that hash value. I got 'tarpley' for the password.

def main():
	Q1A()
	Q2A()
	Q2B()
	Q3A()
	Q4()

if __name__ == "__main__":
	main()

	
