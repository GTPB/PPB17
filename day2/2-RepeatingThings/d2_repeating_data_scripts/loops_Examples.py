##Example 1: print a sequence of text and numbers from 0 to 4

for Count in 0, 1, 2, 3, 4 :
    print "Count is: ", Count

print "Now out of the loop and Count is: ", Count

##Example 2: print a sequence of text and numbers from 0 to 4, using "range()"

for Count in range(4) :
    print "Count is: ", Count

print "Now out of the loop and Count is: ", Count

##Example 3: print a sequence of text and numbers ranging from 2 to 4

for Count in range(2,4) :
    print "Count is: ", Count

print "Now out of the loop and Count is: ", Count

##Example 4: print a sequence of text and numbers ranging from 2 to 5 with 2 numbers interval

for Count in range(2,5,2) :
    print "Count is: ", Count

print "Now out of the loop and Count is: ", Count

##Example 5: Print the number of occurrences of each DNA base in a string

#Method 1 - simple
DNA_String="ACGCATGCATGCATCTTTCATACGGGCTAGCAT"
for Base in ["A", "C", "G", "T"]:
    print DNA_String.count(Base)


#Pseudo-code
Open the file full of DNA/Protein Sequence lines
for each line in turn
....print out the line as a check
....for every type of Base/AA
........print the number of occurances in the current line

#Method 2 - complex
Infile=open("DNA.SEQ")
for Line in Infile:
#    print Line
    for Base in ["A", "C", "G", "T"]:
        print Line.count(Base), Base





