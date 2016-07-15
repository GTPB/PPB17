'''
Parsing - Exercise 14

The script reads the cancer-expressed.txt file and creates and
prints a list containing the ACs listed in the input file. 

'''

cancer_file = open('cancer-expressed.txt')

cancer_list = []

for line in cancer_file:
    # Remove the newline character
    AC = line.strip()
    cancer_list.append(AC)

print cancer_list

