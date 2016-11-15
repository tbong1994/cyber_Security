#hw6

#take in 2 files and do an analysis.
#IN = internet
#@param (record name,ttl,record class,record type,record data)
#if name is empty == same as previous record
#if ttl is empty, global ttl value is assigned

def unique(file_name):
	zone_file = open(file_name, "r") #open file
	
	#count of unique values.
	uniq_name = {}
	uniq_ttl = {}
	uniq_class = {}
	uniq_type = {}
	uniq_data = {}
	
	for line in zone_file:
		line = line.split() #line is an array with 5 elements now.[name,ttl,class,type,data]
		#print line
		
	zone_file.close()

#zone file
unique("../../root.zone")
