#1. marker check------------------------------------------------------------------------------------------------------------------------
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy
marker=['','BRCA1','TGM2','CCND1','EPO','TGFB3','IGF2','BNIP3L','BNIP3','NDRG1']     # marker = input('Enter your marker: ')
for i in range(1,10):
#norm------------------------------------------------------------------------------------------------------------------------------------
    norm = []
    norm = open('BC-TCGA-Normal.txt','r')
    for nline in norm:
        nline = nline.split()
        if (nline[0]) == marker[i]:
            nlinef = [float(item) for item in nline[1:]]
            # nlinef = numpy.log2(nlinef)
            # print(nline)
    norm.close()
#tumor----------------------------------------------------------------------------------------------------------------------------------------------------------------
    tumor = []
    tumor = open('BC-TCGA-Tumor.txt','r')
    for tline in tumor:
        tline = tline.split()
        if  (tline[0]) == marker[i]:
            tlinef = [float(item) for item in tline[1:]]
            # tlinef = numpy.log2(tlinef)
            # print(tline)
    tumor.close()
#Ttest-----------------------------------------------------------------------------------------------------------------------------------------------------------
    print (marker[i],stats.ttest_ind(tlinef,nlinef))
#fig----------------------------------------------------------------------------------------------------------------------------------------------------------------
    plt.subplot(2, 5, i)                                                                # 
    plt.tight_layout()
    plt.title(marker[i], fontsize = 20)
    if i>4:
        plt.xlabel('gene expression level')
    if i==1 or i==6:
        plt.ylabel('density')
    sns.distplot(nlinef,hist=False) 
    sns.distplot(tlinef,hist=False)
plt.show()
print(marker)
