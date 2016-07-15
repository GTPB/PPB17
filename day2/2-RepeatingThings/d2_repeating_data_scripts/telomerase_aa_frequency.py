telomerase = open("telomerase.txt") 

seq = telomerase.read() 

for aa in "ACDEFGHKILMNPQRSTVYW":
    aa_count = seq.count(aa)
    aa_freq = aa_count/float(len(seq)) 
    print "The frequency of", aa, "is:", round(aa_freq, 3)
