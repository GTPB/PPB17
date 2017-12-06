from Bio import Entrez

Entrez.email=''

handle=Entrez.esearch(db='pubmed', term='PyCogent OR RNA', retmax='3')
record=Entrez.read(handle)
print record['IdList']


