F = open('random_distribution.tsv')
O = open('gene_expression.csv', 'w')
O2 = open('gene_expression-few.csv', 'w')

n = 0; m = 0

for line in F:
    n = n + 1
    m = m + 1
    #O.write('gene' + str(n) + ',' + ','.join(line.split('\t')))
    O.write('gene' + str(n) + ',' + line.split('\t')[2] + '\n')
    O2.write('gene' + str(m) + ',' + line.split('\t')[2] + '\n')
    if m == 10: m = 0
O.close()
