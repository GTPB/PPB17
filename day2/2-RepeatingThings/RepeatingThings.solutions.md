#### Solution to challenge #1
```
telomerase = open("telomerase.txt")

seq = telomerase.read()

print seq

for aa in seq:
  print aa
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/2-RepeatingThings/RepeatingThings.md#challenge-1">back<a/>


#### Solution to challenge #2
```
telomerase = open("telomerase.txt")

for line in telomerase:
  print line
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/2-RepeatingThings/RepeatingThings.md#challenge-2">back<a/>


#### Solution to challenge #3
```
telomerase = open("telomerase.txt")

seq = telomerase.read()

for aa in "ACDEFGHKILMNPQRSTVYW":
  aa_count = seq.count(aa)
  aa_freq = aa_count/float(len(seq))
  print aa, round(aa_freq, 3)
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/2-RepeatingThings/RepeatingThings.md#challenge-3">back<a/>
