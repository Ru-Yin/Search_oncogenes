import sys
sys.setrecursionlimit(5000) #設定運轉loop
import tkinter as tk
from tkinter import *
from tkinter import messagebox #載入訊息視窗模組
win = tk.Tk() #建立視窗
win.title("OAIBC(Oncogene Analysis In Breast Cancer)") #建立視窗標題
win.geometry('800x600') #建立視窗大小
win.resizable(True, True) # 如果不想讓使用者能調整視窗大小的話就均設為False
#_______________設定圖片____________________________
from PIL import Image, ImageTk  
img = Image.open('BC2.png') 
img.save('BC2.ico')
win.iconbitmap('BC2.ico') #更改左上角的icon圖示
#_______________function設定____________________________    
def marker_analysis(): #Published oncogene markers 選項紐主執行function
    import os
    os.system('python marker_p-value.py')
def gene_analysis():  #Genetic analysis result 選項紐主執行function
    marker=['BRCA1','TGM2','CCND1','EPO','TGFB3','IGF2','BNIP3L','BNIP3','NDRG1']
    input_gene=e1.get()
    print(input_gene)
    win3=tk.Tk()
    win3.title('Genetic analysis result')
    from total_gene_pvalue import pvalue
    pot, net=pvalue()
    if input_gene in pot:
        p=input_gene+' is positively correlated with oncogenes.'
        lab1=Label(win3,text=p,font=('Comic Sans MS', 20),bg='lightblue',width=100)
        lab1.pack()
    elif input_gene in net:
        n=input_gene+' is negatively correlated with oncogenes.'
        # print('HERE')
        lab1=Label(win3,text=n,font=('Comic Sans MS', 20),bg='lightblue',width=100)
        lab1.pack()
    elif input_gene in marker:
        lab1=Label(win3,text=input_gene+' is published marker.',font=('Comic Sans MS', 20),bg='lightblue',width=100)
        lab1.pack()
     #__________positive correlation part___________________ 
def correlation_analysis(): #Correlation analysis選項紐主執行function
    marker=['BRCA1','TGM2','CCND1','EPO','TGFB3','IGF2','BNIP3L','BNIP3','NDRG1']
    input_gene=e1.get()
    win4=tk.Tk()
    win4.title('correlation result')  
    from positive_correlation import correlation
    nge, tge=correlation()
    if input_gene in tge:
        tt=input_gene+' is Tumor-correlation gene!'
        lab2=Label(win4,text=tt,font=('Comic Sans MS', 20),bg='yellow',width=100)
        lab2.pack()
    elif input_gene in marker:
        lab2=Label(win4,text=input_gene+' is published marker.',font=('Comic Sans MS', 20),bg='lightblue',width=100)
        lab2.pack()
    else:
        t=input_gene+' is normal gene!'
        lab2=Label(win4,text=t,font=('Comic Sans MS', 20),bg='yellow',width=100)
        lab2.pack()
    
def PCA_analysis(): #PCA analysis選項紐主執行function
    import os
    os.system('PCA_tool.py')
def enterInfo(): #Input_function
    input_gene=e1.get()
    norm = []
    norm_t=[]
    norm = open('BC-TCGA-Normal.txt','r')
    for nline in norm:
        nline = nline.split()
        norm_t.append(nline[0])
        
    tumor = []
    tumor_t=[]
    tumor = open('BC-TCGA-Tumor.txt','r')
    for tline in tumor:
        tline = tline.split()
        tumor_t.append(tline[0])
   
    if input_gene in norm_t or input_gene in tumor_t: #核對基因是否在資料庫內
        win=Tk()
        win.title('Menu')
        win.geometry('500x300')
        win.resizable(True, True)
      #__設定按鈕選項______________________________________________________________________________________________________________________  
        tk.Button(win, text="Published oncogene markers",bg='#0052cc',fg='#ffffff', font=('Comic Sans MS', 20), width=30, command=marker_analysis).pack(side=TOP)
        tk.Button(win, text="Genetic analysis result",width=30,bg='#0052cc',fg='#ffffff', font=('Comic Sans MS', 20), command=gene_analysis).pack(side=TOP, pady=5)
        tk.Button(win, text="Correlation analysis",width=30,bg='#0052cc',fg='#ffffff', font=('Comic Sans MS', 20), command=correlation_analysis).pack(side=TOP, pady=5)
        tk.Button(win, text="PCA analysis result",width=30,bg='#0052cc',fg='#ffffff', font=('Comic Sans MS', 20), command=PCA_analysis).pack(side=TOP)

    else: #若搜尋基因不在資料庫內會跳出的訊息框
        from tkinter.messagebox import askretrycancel
        messagebox.askretrycancel('Attention', "Oops!\nI can't find the gene in this database!\n Please enter again~")
    norm.close() 
    tumor.close()
lab1=Label(win,text='Gene name',font=('Comic Sans MS', 20),width=30) #初始視窗的字樣
e1=Entry(win, width=30) #設定搜尋填字框
input_gene=e1.get()    #取得搜尋基因名稱
btn1=Button(win,text="Search",font=('Comic Sans MS', 20),width=20,command=enterInfo) #初始視窗的按鈕選項
btn2=Button(win,text="Quit",font=('Comic Sans MS', 20),width=20,command=win.quit)

img=Image.open("gene.jpg") #設定視窗圖片
img=ImageTk.PhotoImage(img)
imLabel=tk.Label(win,image=img)



lab1.pack() #字樣及按鈕元件位置排序
e1.pack(pady=5)
btn1.pack(pady=5)
btn2.pack()
imLabel.pack()




win.mainloop() # 自動刷新畫面
