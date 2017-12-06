## pattern matching
print "Pattern matching exercise"

print "\n"
print "\n"

import re

seq = 'VSVLTMFRYAGWLDRLYMLVGTQLAAIIHGVALPLMMLI'
pattern = re.compile('[ST]Q')
match = pattern.search(seq)
if match:
 print '%10s' % (seq[match.start() - 4: match.end() + 4])
 print '%6s' % match.group()
else:
 print "no match"


print "\n"
print "\n"

#### Our try

print "TRY 1"
seq1="VSVLTHFRYAGWLDRLTMLYMLVGTQLAAIIHGVALTLLPLMMLIVSVLTMFRYAGWLDLTMRLYMLLTHVGTQLAAIIHGVALPLMMLI"
pattern1=re.compile('LT[MLH]')
match1= pattern1.search(seq1)
all=pattern1.findall(seq1)
print "\n"

print "all matches in our sequence:", all

iter=pattern1.finditer(seq1)

for x in iter:
    print x.group()
    print x.span()
     
print "\n"

if match1:
 print '%9s' % (seq1[match1.start() - 3: match1.end() + 3]), '%5.8f' % 856
 print '%6s' % match1.group()
 print match1.span()
 print match1.start()
 print match1.end()
else:
 print "no match"
