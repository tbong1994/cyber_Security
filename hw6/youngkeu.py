#hw6

#take in 2 files and do an analysis.
#IN = internet
#@param (record name,ttl,record class,record type,record data)
#if name is empty == same as previous record
#if ttl is empty, global ttl value is assigned

record_and_freq = {}  #record dictionary
prob_list = []  #array of probability for each unique record

def unique(file_name):
	zone_file = open(file_name, "r") #open file
	
	#count of unique values.
	uniq_name = 0
	uniq_ttl = 0
	uniq_class = 0
	uniq_type = 0
	uniq_data = 0
	
	for line in pw_file:
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
	
