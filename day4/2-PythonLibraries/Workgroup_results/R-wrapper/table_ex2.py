import rpy2.robjects as robjects
r = robjects.r
f=r("read.table('table.txt', sep=',')")
f_matrix=r("as.matrix("+f.r_repr()+", ncol=4)")
mean_first_col=r.mean(float(f_matrix[0]))
print(mean_first_col)
print (f_matrix)
print (f)
