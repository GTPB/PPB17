'''

Python Programs - Exercise 5

The script reads the telomerase.txt file and prints first the
whole sequence and then the sequence residue by residue.

'''

telomerase = open("telomerase.txt") 

seq = telomerase.read() 

print seq

for aa in seq: 
    print aa
