from Bio import Entrez

Entrez.email=''

handle=Entrez.esearch(db='nucleotide', term='Homo sapiens AND mRNA AND MapK')
records=Entrez.read(handle)
print records['Count']
top3_records=records['IdList'][0:3]
print top3_records
gi_list=','.join(top3_records)
print gi_list
handle=Entrez.efetch(db='nucleotide', id=gi_list, rettype='gb', retmode='xml')
records=Entrez.read(handle)
print len(records)
print records[0].keys()
print records[0]['GBSeq_organism']



