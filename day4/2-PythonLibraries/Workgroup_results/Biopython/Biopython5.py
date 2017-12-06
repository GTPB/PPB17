from Bio import Entrez

Entrez.email=''

handle=Entrez.esearch(db='pubmed', term='PyCogent AND RNA')
record=Entrez.read(handle)
print record['IdList']
handle=Entrez.esearch(db='pubmed', term='PyCogent OR RNA')
record=Entrez.read(handle)
print record['Count']
handle=Entrez.esearch(db='pubmed', term='PyCogent AND 2008[YEAR]')
record=Entrez.read(handle)
print record['IdList']
handle=Entrez.esearch(db='pubmed', term='C. elegans[ORGANISM] AND 2008[YEAR] AND Mapk[Gene]')
record=Entrez.read(handle)
print record['Count']

