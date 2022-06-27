#3. pos correlation----------------------------------------
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
pos=['VEGFA']   
#tumor----------------------------------------
tumor = [] ; genename = []
tumor = open('BC-TCGA-Tumor.txt','r')
for t in tumor:                                                 #find marker
    t = t.split()
    genename.append(t[0])
    if (t[0]) == pos[0]:
        marker = [float(item) for item in t[1:]]
        x = np.array(marker)
tumor.close()

i=0; tumor = []; tgn = []  ;iii=0                                     #reading total gene
tumor = open('BC-TCGA-Tumor.txt','r')
for t in tumor:
    t = t.split()
    iii =iii+1
    if t[1] != 'REF' :
        t = ['0' if ii == 'null' else ii for ii in t]
        ttest = [float(item) for item in t[1:]]
        y = np.array(ttest)
        if (scipy.stats.pearsonr(x, y)[0]) > 0.4:
            tgn.append(genename[iii-1])
            i=i+1
print('Tumor:-correlation gene:',i)#; print(tgn)
tumor.close()

#norm----------------------------------------
norm = [] ; genename = []
norm = open('BC-TCGA-Normal.txt','r')
for n in norm:                                                      #find marker
    n = n.split()
    genename.append(n[0])
    if (n[0]) == pos[0]:
        nmarker = [float(item) for item in n[1:]]
        x = np.array(nmarker)
norm.close()

i=0; norm = [] ; ngn = []  ; iii=0                                        #reading total gene
norm = open('BC-TCGA-Normal.txt','r')
for n in norm:    
    n = n.split()
    iii =iii+1
    if n[1] != 'REF' :
        n = ['0' if ii == 'null' else ii for ii in n]
        ntest = [float(item) for item in n[1:]]
        y = np.array(ntest)
        if (scipy.stats.pearsonr(x, y)[0]) > 0.4:
            ngn.append(genename[iii-1])
            i=i+1
print('Normal-correlation gene:',i) #; print(ngn)
norm.close()





#Overlap----------------------------------------
overlap = ngn and tgn
from matplotlib_venn import venn2
from matplotlib import pyplot as plt
# Venn2
set_a = set(ngn)
set_b = set(tgn)
venn2(subsets=[set_a, set_b],
      set_labels=['normal', 'tumor'],
      set_colors=['blue', 'red'])
plt.title('correlation Overlap', fontsize = 20)
plt.show()

gn = set(ngn) & set(tgn)
ol= list(gn)


#correlation


norm = [] ; genename = []
norm = open('BC-TCGA-Normal.txt','r')
for n in norm:                                                      #find marker
    n = n.split()
    genename.append(n[0])
    if (n[0]) == pos[0]:
        nmarker = [float(item) for item in n[1:]]
        x = np.array(nmarker)
norm.close()
i=0; norm = [] ; ngn = []  ; iii=0                                        #reading total gene
norm = open('BC-TCGA-Normal.txt','r')
for n in norm:    
    n = n.split()
    iii =iii+1
    if n[1] != 'REF' :
        n = ['0' if ii == 'null' else ii for ii in n]
        ntest = [float(item) for item in n[1:]]
        y = np.array(ntest)
        if n[0] in ol :
            ngn.append(genename[iii-1])
            i=i+1
            plt.subplot(3, 5, i)                                #correlation fig
            plt.tight_layout()
            plt.scatter(x, y,s=1) 
            plt.xlabel('VEGFA')
            plt.ylabel(n[0])
plt.show()
norm.close()

#tumor----------------------------------------
tumor = [] ; genename = []
tumor = open('BC-TCGA-Tumor.txt','r')
for t in tumor:                                                 #find marker
    t = t.split()
    genename.append(t[0])
    if (t[0]) == pos[0]:
        marker = [float(item) for item in t[1:]]
        x = np.array(marker)
tumor.close()
i=0; tumor = []; tgn = []  ;iii=0                                     #reading total gene
tumor = open('BC-TCGA-Tumor.txt','r')
for t in tumor:
    t = t.split()
    iii =iii+1
    if t[1] != 'REF' :
        t = ['0' if ii == 'null' else ii for ii in t]
        ttest = [float(item) for item in t[1:]]
        y = np.array(ttest)
        if t[0] in ol :
            tgn.append(genename[iii-1])
            i=i+1
            plt.subplot(3, 5, i)                                #correlation fig
            plt.tight_layout()
            plt.scatter(x, y,s=1) 
            plt.xlabel('VEGFA')
            plt.ylabel(t[0])
plt.show()


# import matplotlib.pyplot as plt
# from matplotlib_venn import venn3
# def venn_diagram(a, b, c, labels=['A', 'B', 'C']):
    
#     a = list(set(a))
#     b = list(set(b))
#     c = list(set(c))
    
#     only_a = len( [x for x in a if x not in b+c] )
#     only_b = len( [x for x in b if x not in a+c] )
#     only_c = len( [x for x in c if x not in a+b] )

#     a_b = len(np.intersect1d(a, b))
#     a_c = len(np.intersect1d(a, c))
#     b_c = len(np.intersect1d(b, c))
    
#     a_b_c = len([ x for x in a if (x in b) and (x in c)])
    
#     venn3(subsets=(only_a, only_b, a_b, only_c, a_c, b_c, a_b_c), set_labels=set_labels)    

# venn_diagram([1, 2], [1, 2, 3, 4], [1, 2, 3])
# time.sleep(1)