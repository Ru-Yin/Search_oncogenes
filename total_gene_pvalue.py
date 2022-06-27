#1. marker check------------------------------------------------------------------------------------------------------------------------
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
# loading database-------------------------------------------------------------------------
norm = [] ; norm = open('BC-TCGA-Normal.txt','r')
tumor = [] ; tumor = open('BC-TCGA-Tumor.txt','r')
nm = [] ; tm = [] ; nt = [] ; tt = []
genename = []
for n in norm:
    n = n.split()
    if n[1] != 'REF':
        genename.append(n[0])
        n = ['0' if x == 'null' else x for x in n]
        nm = [float(item) for item in n[1:]]
    #    n = numpy.log2(n)
        nt.append(nm[1:])
for t in tumor:
    t = t.split()
    if t[1] != 'REF':
        t = ['0' if y == 'null' else y for y in t]
        tm = [float(item) for item in t[1:]]
        # t = numpy.log2(t)
        tt.append(tm[1:])
norm.close() ; tumor.close()
# loading database-------------------------------------------------------------------------
po =0  ; ne =0 
pot = [] ;net = []    
for i in range(17814):
    if stats.ttest_ind(tt[i],nt[i])[1] < 4.7e-16 :
        if stats.ttest_ind(tt[i],nt[i])[0] > 8.35:
            pot.append(genename[i])
            po = po + 1
for i in range(17814):
    if stats.ttest_ind(tt[i],nt[i])[1] < 9.88e-24 :
        if stats.ttest_ind(tt[i],nt[i])[0] < -10.49:
            ne = ne +1
            net.append(genename[i])

# print ('positive gene:',po)
# print(pot)
# print ('negative gene:',ne)
# print(net)
def pvalue():
    return pot, net


# from matplotlib_venn import venn2
# from matplotlib import pyplot as plt
# # Venn2
# set_a = set(ngn )
# set_b = set(tgn)

# venn2(subsets=[set_a, set_b],
#       set_labels=['normal', 'tumor'],
#       set_colors=['blue', 'red'])
# plt.title('Overlap', fontsize = 20)
# plt.show()