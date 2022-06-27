import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 讀取data------------------------------------------------------------
def read_data(file_path):   # 一個讀txt檔，並將其轉為list的function
    title = []
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.replace('null', '0')    # data中有一些值為null，我把它改成0，不然無法轉成float
            data_list = line.split()
            if data_list[0] == 'Hybridization':
                continue    # 跳過病患編號那行
            else:
                title += [data_list[0]]     # title儲存每個基因的名字 (雖然沒用到)
                data_list2 = [float(item) for item in data_list[1:]]    # 將單一一行後面的數據轉成float
                data += [data_list2]    # 整合每一行得到的list
    return title, data

n_title, normal = read_data('BC-TCGA-Normal.txt')
t_title, tumor = read_data('BC-TCGA-Tumor.txt')

# Combine normal data and tumor data-----------------------------------------
n_T = np.array(normal).T    # 把data轉成Numpy array並transpose，在numpy array這種type的後面加上.T能把矩陣轉向
t_T = np.array(tumor).T     # 因為PCA計算時是把column作為變量 (aka 樣本的特徵)
data = np.append(n_T, t_T, axis = 0)    # 合併normal及tumor data

# PCA------------------------------------------------------------------------
pca = PCA(n_components = 2)
# n_components為降維後的維度數量，若不填數字則預設為原矩陣中最小的數字
# 舉例來說，10*50的矩陣，預設中可以降維成10*10，得到PC1-PC10
# 但可以改變n_components來將其降維至10*2，得到PC1及PC2
data_dr = pca.fit_transform(data)   #
print(f'Explained variance ratio: \n\
      PC1: {pca.explained_variance_ratio_[0]:.2%}\n\
      PC2: {pca.explained_variance_ratio_[1]:.2%}')
# 這裡的explained_variance_ratio指的是，降維後的每個主成分所佔的資訊量，佔原始資訊的百分比
# 應該是這樣解釋啦，通常會希望PC1+PC2越高越好，代表PCA能解釋的結果越接近原始數據
# 但用所有的基因 (17814個變量) 去降維後，PC1+PC2只有21%左右
# 如果n_components為預設的話，所有PC的Explained variance ratio的總合會為100%
n_dr, t_dr = data_dr[:len(n_T)], data_dr[len(n_T):]     # 將data_dr拆分回兩個group，以便繪圖

# figure---------------------------------------------------------------------
plt.figure()
plt.title('PCA analysis of breast cancer dataset')  # 圖標題
plt.scatter(n_dr[:,0], n_dr[:,1]    # 畫散佈圖，[:,n]這個是np的寫法，指的是第n個column
            , c = 'blue', s = 8, alpha=0.5     # c = '顏色', s = '大小', alpha = '透明度'
            , label='Normal')   # label為normal，上圖例的時候會用到
plt.scatter(t_dr[:,0], t_dr[:,1]
            , c = 'red', s = 8, alpha=0.5
            , label='Tumor')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%})')     # x, y軸的標題
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%})')
plt.legend()    # 顯示圖例，裡面填參數可以調整圖例的位置
plt.show()