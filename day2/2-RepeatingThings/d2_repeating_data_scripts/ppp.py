import re 
import sys

count=1
for line in open ("/home/enza/ezcngit/python_course/day2/3-Parsing/d2_parsing_data_script/sprot_prot.fasta", "r"): 
	if re.match(">" , line): 
		f=open("/home/enza/ezcngit/python_course/day2/2-RepeatingThings/d2_repeating_data_scripts/seq_fasta/seq.%s.fasta" %(count) , "w") 
		count+=1 
		sys.stdout=f 
		print line.rstrip() 
	else: print line.rstrip()			
