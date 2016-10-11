import os
import math
import hashlib


#global vars
pw_and_freq = {}  #password dictionary
char_and_freq = {} #character dictionary for Q1B
prob_list = []  #array of probability for each unique pw
num_chars=0 #count number of characters for Q1B
num_pwds = 0  #count the num of pwds from the input file

def Q1A():
	pw_file = open("passwords-hw4", "r")
	#output file
	result_file = open("Q1A.txt","w+")
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
##calculate frequency of each character from the file.
def Q1B():
	#add each character and frequency to character freuqnecy dictionary.
	global num_chars
	for pw in pw_and_freq:
		for char in pw:
			if(char<='Z' and char >='A'):
				num_chars +=1 #count characters
				if(char_and_freq.has_key(char)):
					char_and_freq[char]+=1
				else:
					char_and_freq[char] =1
	result_file = open("Q1B.txt","w+")
	for char in char_and_freq:
		result_file.write("{}\t{}\t{:.2f}\n".format(char,char_and_freq[char],ch_prob(char_and_freq[char])))
	result_file.close()
	
#calculate probability of character over all occurences of characters.
def ch_prob(ch_freq):
	probability = float(ch_freq)/float(num_chars)
	prob_in_percent = probability * 100.0
	return float(prob_in_percent)	
	
#calculate probability of pwds in input file
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
	max_entropy = math.log((num_pwds),2)
	result_file = open('Q2B.txt','w+')
	result_file.write("%.3f" %(max_entropy))
	result_file.close()

#repeat Q2A but this time, only unique passwords(multiset from the pws file) out of the first column from pw_and_freq
# num of unique pws = length of dictionary.
def Q3A():
	result_file = open('Q3A.txt','w+')
	entropy = 0.0
	num_of_unique_pw = float(len(prob_list))
	for i in range(len(prob_list)):
		probability = (1.0/num_of_unique_pw)
		entropy += -probability*math.log(probability,2)
	result_file.write("%.3f" %(entropy))
	result_file.close()

def Q3B():
	max_entropy = math.log(len(pw_and_freq),2)
	result_file = open('Q3B.txt','w+')
	result_file.write("%.3f" %(max_entropy))
	result_file.close()

#brute force search for password, given hash values. Dictionary is sorted by frequency(order of likelyhood), so it would take less than O(n), hopefully.
def Q4():
	md5_val = []
	in_file = open('Q4in.txt')
	for line in in_file:
		md5_val.append(line.strip())
	in_file.close()
	result_file = open('Q4.txt','w+')
	
	##This loop will run in O(n x i), n is the number of the input hash values, i is the index for each hashvalue from the password dictionary.
	##Each hash value from the input will be compared to every element in the dictionary until the comparison returns true,
	##when the comparison returns true(it wil return true, because we assume that all the passwords corresponding to the input hash values are inside the dictionary) 
	##it will skip the remaining iterations over the dictionary and move on to the next hash value from
	##the input file. Thus, for each hash value(n), there will be i iterations.

	count = 0 #keep counting until all four md5's have been found.
	
	#sorting dictionary by values (mydict.iteritems(), key=lambda (k,v): (v,k))...
	#reference from http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
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
				return
			i+=1
	result_file.close()

def main():
	Q1A()
	Q1B()
	Q2A()
	Q2B()
	Q3A()
	Q3B()
	Q4()

if __name__ == "__main__":
	main()

	
