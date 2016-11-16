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
	
	#dict for unique lines in the file based on different standards.
	uniq_line_by_type ={}
	uniq_line_by_name={}
	uniq_line_by_ttl={}
	uniq_line_by_class={}
	
	#count of different names associated with unique type.
	diff_name_for_type = {} #pair name:type
	
	for line in zone_file:
		sp_line = line.split() #line is an array with 5 elements now.[name,ttl,class,type,data]
		if(uniq_name.has_key(sp_line[0])):
			uniq_name[sp_line[0]] +=1
		else:
			uniq_name[sp_line[0]] = 1
			#uniq_line_by_name[sp_line[0]] = line
		if(uniq_ttl.has_key(sp_line[1])):
			uniq_ttl[sp_line[1]] +=1
		else:
			uniq_ttl[sp_line[1]] = 1
			#uniq_line_by_ttl[sp_line[1]] = line
		if(uniq_class.has_key(sp_line[2])):
			uniq_class[sp_line[2]] +=1
		else:
			uniq_class[sp_line[2]] = 1
			#uniq_line_by_class[sp_line[2]] = line
			
		if(uniq_type.has_key(sp_line[3])):
			uniq_type[sp_line[3]] +=1
		else:
			uniq_type[sp_line[3]] = 1
			#uniq_line_by_type[sp_line[3]] = line
			
		if(uniq_data.has_key(sp_line[4])):
			uniq_data[sp_line[4]] +=1
		else:
			uniq_data[sp_line[4]] = 1
		
		#for  in sorted(pw_and_freq.iterkeys()):
	#part b
	#LENGTH OF EACH DICTIONARY REPRESENTS # OF UNIQUE VALUES.
	print len(uniq_name)
	print len(uniq_ttl)
	print len(uniq_class)
	print len(uniq_type)
	print len(uniq_data)
	
	#print len(uniq_line_by_name)
	#print len(uniq_line_by_ttl)
	#print len(uniq_line_by_class)
	#print len(uniq_line_by_type)
	
	#part c
	#part d. Count # of different names associated with each type.
	
	
	zone_file.close()
	
#zone file
unique("../../root.zone")
