<a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers#this-repository-is-for-the-course-materials-and-it-is-organized-as-follows"> Back to Timetable</a>




# Searching (and manipulating) your data

<img src="../../img/geneticcode.png" alt="slot" style="width: 300px;"/>

<img src="../../img/datser1.png" alt="slot" style="width: 300px;"/>

<img src="../../img/datser2.png" alt="slot" style="width: 300px;"/>
<img src="../../img/datser3.png" alt="slot" style="width: 300px;"/>
<img src="../../img/datser4.png" alt="slot" style="width: 300px;"/>
<img src="../../img/datser5.png" alt="slot" style="width: 300px;"/>
<img src="../../img/datser6.png" alt="slot" style="width: 300px;"/>
<img src="../../img/datser7.png" alt="slot" style="width: 300px;"/>
<img src="../../img/datser8.png" alt="slot" style="width: 300px;"/>
<img src="../../img/datser9.png" alt="slot" style="width: 300px;"/>

```
codonAMINO =  {'GCU':'A','GCC':'A','GCA':'A', 'GCG':'A',
'CGU':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R','AGG':'R',
'UCU':'S','UCC':'S','UCA':'S','UCG':'S','AGU':'S','AGC':'S',
'AUU':'I','AUC':'I','AUA':'I','AUU':'I','AUC':'I','AUA':'I',
'UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
'GGU':'G','GGC':'G','GGA':'G','GGG':'G','AAU':'N','AAC':'N',
'GUU':'V','GUC':'V','GUA':'V','GUG':'V','GAU':'D','GAC':'D',
'ACU':'T','ACC':'T','ACA':'T','ACG':'T','UGU':'C','UGC':'C',
'CCU':'P','CCC':'P','CCA':'P','CCG':'P','CAA':'Q','CAG':'Q',
'GAA':'E','GAG':'E','CAU':'H','CAC':'H','AAA':'K','AAG':'K',
'UUU':'F','UUC':'F','UAU':'Y','UAC':'Y','AUG':'M','UGG':'W',
'AUG':'START','UAG':'STOP', 'UGA':'STOP', 'UAA':'STOP' }
>>> codonAMINO['GCU']
'A'
>>> codonAMINO['AUG']
’START’
>>> for k in codonAMINO.keys():
...             print k, codonAMINO[k]
GUC V
AUA I
GUA V
GUG V
ACU T
AAC N
etc.
```

## Dictionaries

Dictionaries are **unordered** collections of objects

Dictionaries are structures for mapping immutable objects (keys) on
arbitrary objects (values)

```
d = {key1:value1, key2:value2, …, keyN:valueN}
```

lists and dictionaries cannot be used as dictionary keys!!!!


keys must be **unique**, i.e. the same key cannot be associated to
more than one value

<img src="../../img/datser_method.png" alt="slot" style="width: 300px;"/>

```
>>> d = {'pep1':'MGSNKSKPKDASQRRRSLEPAENVHGAGG', \
    'pep2':'RSLEPAENVHGAGGGAFPASQTPS'}
>>> len(d)
2

>>> d['pep1']
'MGSNKSKPKDASQRRRSLEPAENVHGAGG'

>>> d['pep3'] = 'ASADGHRGPSAAFAPAAA'
>>> d
{'pep1' : 'MGSNKSKPKDASQRRRSLEPAENVHGAGG',
'pep2' : 'RSLEPAENVHGAGGGAFPASQTPS', 'pep3' :
'ASADGHRGPSAAFAPAAA'}
```

```
>>> del d['pep2']
>>> d
{'pep1' : 'MGSNKSKPKDASQRRRSLEPAENVHGAGG',
'pep3' : 'ASADGHRGPSAAFAPAAA'}

>>> d.clear()
>>> d
{ }
```

```
>>> dict = {"a":1, "b":2, "c":3}
>>> dict.keys()     #list of dictionary keys
['a', 'c', 'b']

>>> keys = dict.keys()
>>> keys.sort() #sort keys
['a', 'b', 'c']

>>> dict.values() #list of dictionary values
[1, 3, 2]

>>> dict.items() #tuple of dictionary (key,value) pairs
[('a', 1), ('c', 3), ('b', 2)]

>>> dict.has_key("a")   #True if dict has key "a", else False
True
```


>#### Challenge #1
---
>Using the `codonAMINO` dictonary from `tgac.py` translate the sequence in `rna_seq.fasta`. Use a single reading frame.
>
---

See the <a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day4/DataSearching/DataSearching.solutions.md#solution-to-challenge-1">solution to challenge #1<a/>
<br>
<br>


>#### Challenge #2
---
>Implement program 1 for the three reading frames
>
---

See the <a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day4/DataSearching/DataSearching.solutions.md#solution-to-challenge-1">solution to challenge #2<a/>
<br>
<br>



## Sort values of a dictionary by its keys

```
# sort values of a dictionary by its keys

structures = {
    '2jel':'antibody',
    '1cse':'subtilisin',
    '1ehz':'tRNA(Phe)',
}

def sort_dict_by_keys(data):
    keys = data.keys()
    keys.sort()
    return [data[k] for k in keys]

print sort_dict_by_keys(structures)
```


## Remove redundancy
<img src="../../img/redund1.png" alt="slot" style="width: 300px;"/>

<img src="../../img/redund2.png" alt="slot" style="width: 300px;"/>


```
Q5XXA6                                                Q7Z769
Q9Y5P2                                                Q8CH62
Q14667                                                Q9GZY1
O75387                                                Q9NQQ7
Q8WV07                                                Q14667
Q8CH62                                                Q5XXA6
Q9GZY1                                                Q9Y5P2
Q9NQQ7                                                Q14667
Q8VCX2                                                O75387
Q7Z769                                                Q9Y5P2
Q8CH62                                                Q8WV07
Q14667                                                Q8VCX2
Q9NQQ7                                                Q8CH62
Q14667                                                Q14667
Q9Y5P2                                                Q9NQQ7
```

<img src="../../img/redund3.png" alt="slot" style="width: 300px;"/>

### Sets
Sets are **unordered** collections of unique objects
they are not sequence-like objects and that they cannot contain
identical elements

- Sets do not support indexing and slicing
- `in` and `not in` operators can be used to test an element for
membership in a set.
- Sets are useful for removing duplicates
- Set operations: **intersection, union, difference, symmetrical
difference**


### Create a new set
In order to create a set, the method `set(x)` must be used,
where `x` is a sequence-like object (string, tuple, list)

`add(x)` <br/>
`update(x)` <br/>


| | |
|----|-----|
| `copy()` | creates a copy |
| `pop()`, `remove()`, `discard()`  | remove set elements  |
| `pop()` | deletes a single element randomly |
| `remove(x)` | removes the element `x` and returns a message of error if `x` is not in the set |
| `discard()`  |  removes the element `x` without returning any error message if `x` is not in the set |

## S1.union(S2)
The `union()` between 2 sets S1 and S2 creates a new set
with the elements from both S1 and S2.

```
>>> S1 = set(['a','b','c'])
>>> S2 = set (['c','d','e'])
>>> S1.union(S2)
set(['a', 'c', 'b', 'e', 'd'])
>>> S1 | S2
set(['a', 'c', 'b', 'e', 'd'])
```

## S1.intersection(S2)

The `intersection()` of 2 sets S1 and S2 creates a new set
with the elements common to S1 and S2

```
>>> S1 = set(['a','b','c'])
>>> S2 = set (['c','d','e'])
>>> S1.intersection(S2)
set(['c'])
>>> S1 & S2
set(['c'])
```
## S1.symmetric_difference(S2)or S1 ^ S2

`symmetric_difference()` of two sets S1 and S2 creates a new set with elements in either S1 or S2 but not both

```
>>> S1 = set(['a','b','c'])
>>> S2 = set (['c','d','e'])
>>> S1.symmetric_difference(S2)
set(['a', 'b', 'e', 'd'])
>>> S1 ^ S2
set(['a', 'b', 'e', 'd'])
```

## S1.difference(S2) or S1 - S2

The  `difference()`  of  two  sets  S1  and  S2  creates  a  new  set with elements in S1 but not in S2

```
>>> S1 = set(['a','b','c'])
>>> S2 = set (['c','d','e'])
>>> S1.difference(S2)
set(['a', 'b'])
>>> S1 - S2
set(['a', 'b'])
>>> S2 – S1
set(['e', 'd'])
```
