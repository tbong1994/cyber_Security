#hw6

#take in 2 files and do an analysis.
#IN = internet
#@param (record name,ttl,record class,record type,record data)
#if name is empty == same as previous record
#if ttl is empty, global ttl value is assigned

def unique(file_name):
	
	#part a
	zone_file = open(file_name, "r") #open file
	
	#count of unique values.
	uniq_name = {}
	uniq_ttl = {}
	uniq_class = {}
	uniq_type = {}
	uniq_data = {}
	
	#count of different names associated with unique type.
	diff_name_for_type = {} #pair name:type
	
	for line in zone_file:
		line = line.split() #line is an array with 5 elements now.[name,ttl,class,type,data]
		if(uniq_name.has_key(line[0])):
			uniq_name[line[0]] +=1
		else:
			uniq_name[line[0]] = 1
		if(uniq_ttl.has_key(line[1])):
			uniq_ttl[line[1]] +=1
		else:
			uniq_ttl[line[1]] = 1
			
		if(uniq_class.has_key(line[2])):
			uniq_class[line[2]] +=1
		else:
			uniq_class[line[2]] = 1
			
		if(uniq_type.has_key(line[3])):
			uniq_type[line[3]] +=1
		else:
			uniq_type[line[3]] = 1
			
		if(uniq_data.has_key(line[4])):
			uniq_data[line[4]] +=1
		else:
			uniq_data[line[4]] = 1
		
	#part b
	#LENGTH OF EACH DICTIONARY REPRESENTS # OF UNIQUE VALUES.
	print len(uniq_name)
	print len(uniq_ttl)
	print len(uniq_class)
	print len(uniq_type)
	print len(uniq_data)
	
	#part c
	#part d. Count # of different names associated with each type.
	
	
	
	
	zone_file.close()

#zone file
unique("../../root.zone")
