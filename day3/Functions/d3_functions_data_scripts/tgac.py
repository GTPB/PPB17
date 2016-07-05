# alcohol dehydrogenase - ahd4 - amino acid sequence
S_prot = "mgtkgkvikckaaiaweagkplcieevevappkahevriqiiatslchtdatvidskfeglafpvivgheaagivesigpgvtnvkpgdkviplyaplcrkckfclspltnlcgkisnlkspasdqqlmedktsrftckgkpvyhffgtstfsqytvvsdinlakidddanlervcllgcgfstgygaainnakvtpgstcavfglggvglsavmgckaagasriigidinsekfvkakalgatdclnprdlhkpiqeviieltkggvdfaldcaggsetmkaaldcttagwgsctfigvaagskgltifpeeliigrtingtffggwksvdsipklvtdyknkkfnldalvthtlpfdkiseafdlmnqgksvrtilif" 

aa = ['A','C','D','E','F','G','H', 'K','I','L','M','N','P','Q','R','S','T','V','Y','W']
aa_hydrofobic = ['A', 'F', 'G', 'I', 'L', 'M', 'P', 'V', 'W']
aa_hydrofile = ['C', 'N', 'Q', 'S', 'T', 'Y']
aa_basic = ['H', 'K', 'R']
aa_acid = ['D', 'E']

S_dna = "gatcctccatatacaacggtatctccacctcaggtttagatctcaacaacggaaccattgccgacatgagacagttaggtatcgtcgagagttacaagctaaaacgagcagtagtcagctctgcatctgaagccgctgaagttctactaagggtggataacatcatccgtgcaagaccaagaaccgccaatagacaacatatgtaacatatttaggatatacctcgaaaataataaaccgccacactgtcattattataattagaaacagaacgcaaaaattatccactatataattcaaagacgcgaaaaaaaaagaacaacgcgtcatagaacttttggcaattcgcgtcacaaataaattttggcaacttatgtttcctcttcgagcagtactcgagccctgtctcaagaatgtaataatacccatcgtaggtatggttaaagatagcatctccacaacctcaaagctccttgccgagagtcgccctcctttgtcgagtaattttcacttttcatatgagaacttattttcttattctttactctcacatcctgtagtgattgacactgcaacagccaccatcactagaagaacagaacaattacttaatagaaaaattatatcttcctcgaaacgatttcctgcttccaacatctacgtatatcaagaagcattcacttaccatgacacagcttcagatttcattattgctgacagctactatatcactactccatctagtagtggccacgccctatgaggcatatcctatcggaaaacaataccccccagtggcaagagtcaatgaatcgtttacatttcaaatttccaatgatacctataaatcgtctgtagacaagacagctcaaataacatacaattgcttcgacttaccgagctggctttcgtttgactctagttctagaacgttctcaggtgaaccttcttctgacttactatctgatgcgaacaccacgttgtatttcaatgtaatactcgagggtacggactctgccgacagcacgtctttgaacaatacataccaatttgttgttacaaaccgtccatccatctcgctatcgtcagatttcaatctattggcgttgttaaaaaactatggttatactaacggcaaaaacgctctgaaactagatcctaatgaagtcttcaacgtgacttttgaccgttcaatgttcactaacgaagaatccattgtgtcgtattacggacgttctcagttgtataatgcgccgttacccaattggctgttcttcgattctggcgagttgaagtttactgggacggcaccggtgataaactcggcgattgctccagaaacaagctacagttttgtcatcatcgctacagacattgaaggattttctgccgttgaggtagaattcgaattagtcatcggggctcaccagttaactacctctattcaaaatagtttgataatcaacgttactgacacaggtaacgtttcatatgacttacctctaaactatgtttatctcgatgacgatcctatttcttctgataaattgggttctataaacttattggatgctccagactgggtggcattagataatgctaccatttccgggtctgtcccagatgaattactcggtaagaactccaatcctgccaatttttctgtgtccatttatgatacttatggtgatgtgatttatttcaacttcgaagttgtctccacaacggatttgtttgccattagttctcttcccaatattaacgctacaaggggtgaatggttctcctactattttttgccttctcagtttacagactacgtgaatacaaacgtttcattagagtttactaattcaagccaagaccatgactgggtgaaattccaatcatctaatttaacattagctggagaagtgcccaagaatttcgacaagctttcattaggtttgaaagcgaaccaaggttcacaatctcaagagctatattttaacatcattggcatggattcaaagataactcactcaaaccacagtgcgaatgcaacgtccacaagaagttctcaccactccacctcaacaagttcttacacatcttctacttaccagtttatccattgcttccttcagtttggcttcactgtcttctagctgttgttctagatcctggtttttcttggtgtagttctcattattagatctcaagttattggagtcttcagccaattgctttgtatcagacaattgactctctaacttctccacttcactgtcgagttgctcgtttttagcggacaaagatttaatctcgttttctttttcagtgttagattgctctaattctttgagctgttctctcagctcctcatatttttcttgccatgactcagattctaattttaagctattcaatttctctttgatc"

dna_symbols =  ['A', 'G', 'C', 'T']

distancePoint = [('N-ALA-1', 42.471, 29.826, 88.811), ('CA-ALA-1', 43.646, 30.725, 88.954), ('C-ALA-1', 44.095, 30.664, 90.419), ('O-ALA-1', 43.363, 30.177, 91.284), 
		     ('CB-ALA-1', 43.280, 32.145, 88.564), ('N-ASN-2', 45.290, 31.175, 90.697), ('CA-ASN-2', 45.839, 31.111, 92.046), ('C-ASN-2', 46.093, 32.391, 92.816), 
		     ('O-ASN-2', 46.812, 33.276, 92.355), ('CB-ASN-2', 47.141, 30.322, 92.019), ('CG-ASN-2', 46.929, 28.881, 91.678), ('OD1-ASN-2', 45.862, 28.322, 91.929),
		     ('ND2-ASN-2', 47.940, 28.262, 91.099), ('N-ALA-3', 45.502, 32.474, 94.000), ('CA-ALA-3', 45.704, 33.611, 94.891), ('C-ALA-3', 46.318, 33.061, 96.196), 
		     ('O-ALA-3', 46.318, 31.847, 96.415), ('CB-ALA-3', 44.380, 34.287, 95.174), ('N-PHE-4', 46.834, 33.949, 97.048), ('CA-PHE-4', 47.440, 33.579, 98.331), 
		     ('C-PHE-4', 46.494, 32.722, 99.185), ('0-PHE-4', 45.371, 33.128, 99.497), ('CB-PHE-4', 47.860, 34.858, 99.094), ('CG-PHE-4', 48.252, 34.641, 100.527), 
		     ('CD1-PHE-4', 49.531, 34.210, 100.858), ('CD2-PHE-4', 47.337, 34.867, 101.550), ('CD1-PHE-4', 49.901, 34.019, 102.187), ('CE2-PHE-4', 47.696, 34.679, 102.884), 
		     ('CZ-PHE-4', 48.985, 34.262, 103.200), ('N-LEU-5', 46.973, 31.535, 99.553) ]


FastaF = [ 	'>MT dna_rm:chromosome chromosome:GRCh37:MT:1:16569:1', 'GATCACAGGTCTATCACCCTATTAACCACTCACGGGAGCTCTCCATGCATTTGGTATTTT', 'CGTCTGGGGGGTATGCACGCGATAGCATTGCGAGACGCTGGAGCCGGAGCACCCTATGTC',
	'GCAGTATCTGTCTTTGATTCCTGCCTCATCCTATTATTTATCGCACCTACGTTCAATATT', 'ACAGGCGAACATACTTACTAAAGTGTGTTAATTAATTAATGCTTGTAGGACATAATAATA', 'ACAATTGAATGTCTGCACAGCCACTTTCCACACAGACATCATAACAAAAAATTTCCACCA',
	'AACCCCCCCTCCCCCGCTTCTGGCCACAGCACTTAAACACATCTCTGCCAAACCCCAAAA', 'ACAAAGAACCCTAACACCAGCCTAACCAGATTTCAAATTTTATCTTTTGGCGGTATGCAC', 'TTTTAACAGTCACCCCCCAACTAACACATTATTTTCCCCTCCCACTCCCATACTACTAAT',
	'CTCATCAATACAACCCCCGCCCATCCTACCCAGCACACACACACCGCTGCTAACCCCATA', 'CCCCGAACCAACCAAACCCCAAAGACACCCCCCACAGTTTATGTAGCTTACCTCCTCAAA', 'GCAATACACTGAAAATGTTTAGACGGGCTCACATCACCCCATAAACAAATAGGTTTGGTC',
	'CTAGCCTTTCTATTAGCTCTTAGTAAGATTACACATGCAAGCATCCCCGTTCCAGTGAGT', 'TCACCCTCTAAATCACCACGATCAAAAGGAACAAGCATCAAGCACGCAGCAATGCAGCTC', 'AAAACGCTTAGCCTAGCCACACCCCCACGGGAAACAGCAGTGATTAACCTTTAGCAATAA',
	'ACGAAAGTTTAACTAAGCTATACTAACCCCAGGGTTGGTCAATTTCGTGCCAGCCACCGC', 'GGTCACACGATTAACCCAAGTCAATAGAAGCCGGCGTAAAGAGTGTTTTAGATCACCCCC', 'TCCCCAATAAAGCTAAAACTCACCTGAGTTGTAAAAAACTCCAGTTGACACAAAATAGAC',
	'TACGAAAGTGGCTTTAACATATCTGAACACACAATAGCTAAGACCCAAACTGGGATTAGA', 'TACCCCACTATGCTTAGCCCTAAACCTCAACAGTTAAATCAACAAAACTGCTCGCCAGAA', 'CACTACGAGCCACAGCTTAAAACTCAAAGGACCTGGCGGTGCTTCATATCCCTCTAGAGG',
	'AGCCTGTTCTGTAATCGATAAACCCCGATCAACCTCACCACCTCTTGCTCAGCCTATATA', 'CCGCCATCTTCAGCAAACCCTGATGAAGGCTACAAAGTAAGCGCAAGTACCCACGTAAAG', 'ACGTTAGGTCAAGGTGTAGCCCATGAGGTGGCAAGAAATGGGCTACATTTTCTACCCCAG',
	'AAAACTACGATAGCCCTTATGAAACTTAAGGGTCGAAGGTGGATTTAGCAGTAAACTAAG', 'AGTAGAGTGCTTAGTTGAACAGGGCCCTGAAGCGCGTACACACCGCCCGTCACCCTCCTC', 'AAGTATACTTCAAAGGACATTTAACTAAAACCCCTACGCATTTATATAGAGGAGACAAGT',
	'CGTAACATGGTAAGTGTACTGGAAAGTGCACTTGGACGAACCAGAGTGTAGCTTAACACA', 'AAGCACCCAACTTACACTTAGGAGATTTCAACTTAACTTGACCGCTCTGAGCTAAACCTA', 'GCCCCAAACCCACTCCACCTTACTACCAGACAACCTTAGCCAAACCATTTACCCAAATAA',
	'AGTATAGGCGATAGAAATTGAAACCTGGCGCAATAGATATAGTACCGCAAGGGAAAGATG', 'AAAAATTATAACCAAGCATAATATAGCAAGGACTAACCCCTATACCTTCTGCATAATGAA', 'TTAACTAGAAATAACTTTGCAAGGAGAGCCAAAGCTAAGACCCCCGAAACCAGACGAGCT',
	'ACCTAAGAACAGCTAAAAGAGCACACCCGTCTATGTAGCAAAATAGTGGGAAGATTTATA', 'GGTAGAGGCGACAAACCTACCGAGCCTGGTGATAGCTGGTTGTCCAAGATAGAATCTTAG', 'TTCAACTTTAAATTTGCCCACAGAACCCTCTAAATCCCCTTGTAAATTTAACTGTTAGTC',
	'CAAAGAGGAACAGCTCTTTGGACACTAGGAAAAAACCTTGTAGAGAGAGTAAAAAATTTA', 'ACACCCATAGTAGGCCTAAAAGCAGCCACCAATTAAGAAAGCGTTCAAGCTCAACACCCA', 'CTACCTAAAAAATCCCAAACATATAACTGAACTCCTCACACCCAATTGGACCAATCTATC',
	'ACCCTATAGAAGAACTAATGTTAGTATAAGTAACATGAAAACATTCTCCTCCGCATAAGC', 'CTGCGTCAGATTAAAACACTGAACTGACAATTAACAGCCCAATATCTACAATCAACCAAC', 'AAGTCATTATTACCCTCACTGTCAACCCAACACAGGCATGCTCATAAGGAAAGGTTAAAA',
	'AAAGTAAAAGGAACTCGGCAAATCTTACCCCGCCTGTTTACCAAAAACATCACCTCTAGC', 'ATCACCAGTATTAGAGGCACCGCCTGCCCAGTGACACATGTTTAACGGCCGCGGTACCCT', 'AACCGTGCAAAGGTAGCATAATCACTTGTTCCTTAAATAGGGACCTGTATGAATGGCTCC',
	'ACGAGGGTTCAGCTGTCTCTTACTTTTAACCAGTGAAATTGACCTGCCCGTGAAGAGGCG' ]

SIMBOLI2 =  {'ALA':'A','CYS':'C','ASP':'D',
         'GLU':'E','PHE':'F','GLY':'G',
         'HIS':'H','LYS':'K','ILE':'I',
         'LEU':'L','MET':'M','ASN':'N',
         'PRO':'P','GLN':'Q','ARG':'R',
         'SER':'S','THR':'T','VAL':'V',
         'TYR':'Y','TRP':'W','XXX':'X'}

propensities = {'N' : 0.22989, 'P': 0.55232, 'Q': -0.187677,
	        'A': -0.26154, 'R': -0.17659, 'S': 0.14288,
	        'C': -0.015152,'T': 0.0088780, 'D': 0.22763,
	        'E': -0.20469, 'V': -0.38618, 'F': -0.22557,
	        'W': -0.243375,'G': 0.43323, 'H': -0.0012174,
	        'Y': -0.20751, 'I': -0.42224, 'K': -0.100092,
	        'L': -0.33793,'M': -0.22590} 

codonAMINO =  {	'GCU':'A','GCC':'A','GCA':'A', 'GCG':'A',
         	   	'CGU':'R','CGC':'R','CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 
		      'AAU':'N','AAC':'N',
		      'GAU':'D','GAC':'D',
 		      'UGU':'C','UGC':'C',
		      'CAA':'Q','CAG':'Q',
		      'GAA':'E','GAG':'E',
         	   	'GGU':'G','GGC':'G','GGA':'G', 'GGG':'G', 
		      'CAU':'H','CAC':'H',
		      'AUU':'I','AUC':'I', 'AUA':'I',
         	   	'UUA':'L','UUG':'L','CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
		      'AAA':'K','AAG':'K',
		      'AUG':'M',
		      'UUU':'F','UUC':'F',
 		      'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
		      'UCU':'S','UCC':'S','UCA':'S','UCG':'S','AGU':'S', 'AGC':'S', 
		      'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
			'UGG':'W', 
			'UAU':'Y', 'UAC':'Y',
			'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
			'UAG':'STOP', 'UGA':'STOP', 'UAA':'STOP' }

