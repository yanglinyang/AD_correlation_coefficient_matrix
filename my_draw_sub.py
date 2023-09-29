# writer:gaozi
# createTime:2023/7/20 16:20
# fileName:my_draw_sub.py
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

titles = ['Incipient-Control','Moderate-Control','Severe-Control']
file_path = r'..\\dataset\\AD病标准化数据.xlsx'   # r对路径进行转义，windows需要
sheetName = 'sub_sc' #
gene_order = pd.read_excel(file_path, sheet_name=[sheetName], header=0)  #读取单元表
cns = 0
#绘制差值的代码
for k in range(2,5):
    x1=(gene_order[sheetName].iloc[:,0:1]).values # 读取基因序号作为x轴
    a,b = [],[]
    for i in x1:
        a.append(i[0])
    y1=(gene_order[sheetName].iloc[:,k-1:k]).values #读取y轴数据
    for i in y1:
        b.append(i[0])
    x=range(1,len(a)+1)
    # print(len(x),len(b))
    # plt.xticks(x, x_label)#绘制x刻度标签
    plt.title(titles[cns])
    ax=plt.gca()
    ax.get_xaxis().set_visible(False)
    plt.bar(x, b, width=2, bottom=None,color=['#1F77B4'])
    plt.savefig('Sub_sc_'+titles[cns]+'.pdf', format='pdf')
    cns += 1
    plt.show()