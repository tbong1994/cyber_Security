#hw6
from collections import OrderedDict
import math
#take in 2 files and do an analysis.
#IN = internet
#@param (record name,ttl,record class,record type,record data)
#if name is empty == same as previous record
#if ttl is empty, global ttl value is assigned

def unique(file_name1, file_name2):
	#part a
	zone_file = open(file_name1, "r") #open file
	#count of unique lines
	uniq_lines = {} # '.' means same as previous 
	
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
	diff_name_for_class={} # class:[]
	diff_name_for_type = {} # type:[]
	diff_name_for_ttl={}# ttl:[]
	diff_name_for_data={}# data:[]
	
	count_of_records = 0 #every line is unique in this file, so just count the lines.
	#prev_name = ""
	for line in zone_file:
		count_of_records +=1
		sp_line = line.split() #line is an array with 5 elements now.[name,ttl,class,type,data]
		if(uniq_name.has_key(sp_line[0])):
			uniq_name[sp_line[0]] +=1
		#elif(len(sp_line[0])==1):
			#uniq_name[prev_name]+=1
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
		
		#for part c,d you can have a separate Dictionary(diff_names_for_type,etc) that saves record type as the key, and 
		#value for the key is either an array or a dictionary.
		#you can check each line and if diff_names_for_type has typeA as a key already, if yes, then check the value(array or dictionary) and 
		#check if record name is already in that array or dictionary. if yes, then discard, if no, then add it to the array or dict.
		#do this for parts c,d. 
		
		#PART D
		if(diff_name_for_type.has_key(sp_line[3])): 
			#print sp_line[3]
			#if(sp_line[3]=='SOA'):
				#print sp_line[0]
			names = diff_name_for_type[sp_line[3]] #dictionary of {type:{names:#}}
			if(names.has_key(sp_line[0])):
				#diff_name_for_type[sp_line[3]][sp_line[0]] +=1
				names[sp_line[0]] +=1
			else:
				names[sp_line[0]] = 1
		else:
			diff_name_for_type.setdefault(sp_line[3], {sp_line[0]:1})
			#print sp_line[3]
		
		
		#PART C
		
		if(diff_name_for_class.has_key(sp_line[2])): 
			#print sp_line[3]
			#if(sp_line[3]=='SOA'):
				#print sp_line[0]
			names = diff_name_for_class[sp_line[2]] #dictionary of {class:{names:#}}
			if(names.has_key(sp_line[0])):
				#diff_name_for_type[sp_line[3]][sp_line[0]] +=1
				names[sp_line[0]] +=1
			else:
				names[sp_line[0]] = 1
		else:
			diff_name_for_class.setdefault(sp_line[2], {sp_line[0]:1})
		
		#PART E 
		
		if(diff_name_for_ttl.has_key(sp_line[1])): 
			#print sp_line[3]
			#if(sp_line[3]=='SOA'):
				#print sp_line[0]
			names = diff_name_for_ttl[sp_line[1]] #dictionary of {ttl:names:#}}
			if(names.has_key(sp_line[0])):
				#diff_name_for_type[sp_line[3]][sp_line[0]] +=1
				names[sp_line[0]] +=1
			else:
				names[sp_line[0]] = 1
		else:
			diff_name_for_ttl.setdefault(sp_line[1], {sp_line[0]:1})
			
		
		#PART F 
		
		if(diff_name_for_data.has_key(sp_line[4])): 
			#print sp_line[3]
			#if(sp_line[3]=='SOA'):
				#print sp_line[0]
			names = diff_name_for_data[sp_line[4]] #dictionary of {data:{names:#}}
			if(names.has_key(sp_line[0])):
				#diff_name_for_type[sp_line[3]][sp_line[0]] +=1
				names[sp_line[0]] +=1
			else:
				names[sp_line[0]] = 1
		else:
			diff_name_for_data.setdefault(sp_line[4], {sp_line[0]:1})
	zone_file.close()
	#part a and b
	#LENGTH OF EACH DICTIONARY REPRESENTS # OF UNIQUE VALUES.
	
	#PART A PRINT 
	#print "%s : %d" %("number of records: ",count_of_records)
	
	#PART B PRINT
	#print ("%s%d" %("unique records: ",count_of_records))
	#print ("%s%d" %("unique names: ",len(uniq_name)))
	#print ("%s%d" %("unique ttl: ",len(uniq_ttl)))
	#print ("%s%d" %("unique class: ",len(uniq_class)))
	#print ("%s%d" %("unique type: ",len(uniq_type)))
	#print ("%s%d" %("unique data: ",len(uniq_data)))

	
	#PART C PRINT
	#for i in sorted(diff_name_for_class): #sort by name
		#print "%s : %d" %(i,len(diff_name_for_class[i]))
		
	
	#PART D PRINT
	#for i in sorted(diff_name_for_type): #sort by name
		#print "%s : %d" %(i,len(diff_name_for_type[i]))
	
	#PART E PRINT ===== SORT BY LIKELYHOOD (VALUE)
	
	#print_dict={}
	#for i in sorted(diff_name_for_ttl):
		#print_dict[i]=len(diff_name_for_ttl[i])
	#descending_ttl = OrderedDict(sorted(print_dict.items(), key=lambda k: k[1], reverse=True)) #sort by value in descending order.
	#for i in descending_ttl:
		#print "%s %s : %s %s" %("TTL_Value",i,"count:",descending_ttl[i])
	#print count_of_records
	
	
	#PART F PRINT
	#for i in sorted(diff_name_for_data): #sort by name
		#print "%s : %d" %(i,len(diff_name_for_data[i]))
	
	
	###OPEN THE NET FILE NOW===
	
	net_file = open(file_name2, "r") #open file	
	
	#count of unique values.
	uniq_name_net = {}
	uniq_ttl_net = {}
	uniq_class_net = {}
	uniq_type_net = {}
	uniq_data_net = {}
	
	#dict for unique lines in the file based on different standards.
	uniq_line_by_type_net ={}
	uniq_line_by_name_net={}
	uniq_line_by_ttl_net={}
	uniq_line_by_class_net={}
	
	#count of different names associated with unique type.
	diff_name_for_class_net={} # class:[]
	diff_name_for_type_net = {} # type:[]
	diff_name_for_ttl_net={}# ttl:[]
	diff_name_for_data_net={}# data:[]
	
	count_of_records_net = 0 #every line is unique in this file, so just count the lines.
	#prev_name = ""
	only_five = 0
	for line in net_file:
		if(line!='\n'): #ignore empty lines
			sp_line = line.split() #line is more complex. get rid of the ones you don't need.
			if(sp_line[0][0]=='$' or sp_line[0][0] == ';'): #don't need such lines
				if(sp_line[0]=='$TTL'):
					if(uniq_ttl_net.has_key(sp_line[1])):
						uniq_ttl_net[sp_line[1]] += 1
					else:
						uniq_ttl_net[sp_line[1]] = 1
				continue
				#continue
			if(len(sp_line)<3 or len(sp_line)>3):
				continue
			else:#these lines are what we need. 3 tuple(name, type, data(domain names))
				count_of_records_net +=1
				#print line
				if(uniq_name_net.has_key(sp_line[0])):
					uniq_name_net[sp_line[0]] +=1
				#elif(len(sp_line[0])==1):
					#uniq_name[prev_name]+=1
				else:
					uniq_name_net[sp_line[0]] = 1
					#uniq_line_by_name[sp_line[0]] = line
				if(uniq_type_net.has_key(sp_line[1])):
					uniq_type_net[sp_line[1]] +=1
				else:
					uniq_type_net[sp_line[1]] = 1
					#uniq_line_by_ttl[sp_line[1]] = line
				if(uniq_data_net.has_key(sp_line[2])):
					uniq_data_net[sp_line[2]] +=1
				else:
					uniq_data_net[sp_line[2]] = 1
					#uniq_line_by_class[sp_line[2]] = line
				
		##for part c,d you can have a separate Dictionary(diff_names_for_type,etc) that saves record type as the key, and 
		##value for the key is either an array or a dictionary.
		##you can check each line and if diff_names_for_type has typeA as a key already, if yes, then check the value(array or dictionary) and 
		##check if record name is already in that array or dictionary. if yes, then discard, if no, then add it to the array or dict.
		##do this for parts c,d. 
		
		##PART D
		if(diff_name_for_type_net.has_key(sp_line[1])): 
			names = diff_name_for_type_net[sp_line[1]] #dictionary of {type:{names:#}}
			if(names.has_key(sp_line[0])):
				names[sp_line[0]] +=1
			else:
				names[sp_line[0]] = 1
		else:
			diff_name_for_type_net.setdefault(sp_line[1], {sp_line[0]:1})
			#print sp_line[3]
		
		
		##PART C
		
		#if(diff_name_for_class_net.has_key(sp_line[2])): 
			#names = diff_name_for_class_net[sp_line[2]] #dictionary of {class:{names:#}}
			#if(names.has_key(sp_line[0])):
				#names[sp_line[0]] +=1
			#else:
				#names[sp_line[0]] = 1
		#else:
			#diff_name_for_class_net.setdefault(sp_line[2], {sp_line[0]:1})
		
		##PART E 
		
		#if(diff_name_for_ttl_net.has_key(sp_line[1])): 
			
			#names = diff_name_for_ttl_net[sp_line[1]] #dictionary of names
			#if(names.has_key(sp_line[0])):
				#names[sp_line[0]] +=1
			#else:
				#names[sp_line[0]] = 1
		#else:
			#diff_name_for_ttl_net.setdefault(sp_line[1], {sp_line[0]:1})
			
		
		##PART F 
		
		if(diff_name_for_data_net.has_key(sp_line[2])): 
			names = diff_name_for_data_net[sp_line[2]] #dictionary of {data:{names:#}}
			if(names.has_key(sp_line[0])):
				names[sp_line[0]] +=1
			else:
				names[sp_line[0]] = 1
		else:
			diff_name_for_data_net.setdefault(sp_line[2], {sp_line[0]:1})
			
			
	net_file.close()
	#part a and b
	#LENGTH OF EACH DICTIONARY REPRESENTS # OF UNIQUE VALUES.
	
	#PART A PRINT 
	print "%s : %d" %("number of records: ",count_of_records_net)
	
	#PART B PRINT
	print ("%s%d" %("unique names: ",len(uniq_name_net)))
	print ("%s%d" %("unique ttl: ",len(uniq_ttl_net)))
	#print ("%s%d" %("unique class: ",len(uniq_class_net)))
	print ("%s%d" %("unique type: ",len(uniq_type_net)))
	print ("%s%d" %("unique data: ",len(uniq_data_net)))
	
	#for i in uniq_name_net:
		#print i
	
	#PART C PRINT
	#for i in sorted(diff_name_for_class): #sort by name
		#print "%s : %d" %(i,len(diff_name_for_class[i]))
		
	
	#PART D PRINT
	for i in sorted(diff_name_for_type_net): #sort by name
		print "%s : %d" %(i,len(diff_name_for_type_net[i]))
	
	#PART E PRINT ===== SORT BY LIKELYHOOD (VALUE)
	
	#print_dict_net={}
	#for i in sorted(diff_name_for_ttl_net):
		#print_dict_net[i]=len(diff_name_for_ttl_net[i])
	#descending_ttl_net = OrderedDict(sorted(print_dict_net.items(), key=lambda k: k[1], reverse=True)) #sort by value in descending order.
	#for i in descending_ttl_net:
		#print "%s %s : %s %s" %("TTL_Value",i,"count:",descending_ttl_net[i])
	#print count_of_records_net
	
	
	#PART F PRINT
	for i in sorted(diff_name_for_data_net): #sort by name
		print "%s : %d" %(i,len(diff_name_for_data_net[i]))
	
	
unique("../../root.zone", "../../net.zone")

def entropy(file_name):
	zone_file = open(file_name, "r") #open file
	
	num_of_lines = 0 #total_range for probability calculation.
	num_of_name = {} #pair of domain name and count
	#entropy of each domain name.
	#entropy = sum of [probablity*log(probability)] for each domain.
	
	for line in zone_file:
		num_of_lines+=1
		sp_line = line.split()
		if(num_of_name.has_key(sp_line[0])):
			num_of_name[sp_line[0]] +=1
		else:
			num_of_name[sp_line[0]] = 1
	zone_file.close()
	#output format = (domain name'\t'entropy)
	
	#total_entropy = 0.0
	for name in num_of_name:
		prob = calc_prob(num_of_name[name],num_of_lines)
		print "%s\t%.5f" %(name,-prob*math.log(prob,2))

	#print total_entropy
	
def calc_prob(val,total_range):
	return float(val)/float(total_range)
	
#entropy("../../root.zone")
