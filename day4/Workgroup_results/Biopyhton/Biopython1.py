from Bio import Entrez
from Bio import Medline
keyword='PyCogent'
Entrez.email=''
handle=Entrez.esearch(db='pubmed', term=keyword)
record=Entrez.read(handle)
pmids=record['IdList']
print pmids
handle=Entrez.efetch(db='pubmed', id=pmids, \
    rettype='medline', retmode='text')
medline_records=Medline.parse(handle)
records=list(medline_records)
n=1
for record in records:
    if keyword in record['TI']:
        print n, ')', record['TI']
        n += 1
