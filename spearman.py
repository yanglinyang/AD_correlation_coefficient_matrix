import os
from typing import Type
import openpyxl
import pandas as pd
import numpy as np
import scipy.stats

file_path = r'.\\dataset\\AD病标准化数据.xlsx'   # r对路径进行转义，windows需要
gene_data = pd.read_excel(file_path, sheet_name=['Con','Mod','Inc','Sev'], header=1, index_col=0)
result_spear=[]
for i in gene_data['Con'].index:
    # print((gene_data['Con'].loc[i]).values)
    L1_Con=(gene_data['Con'].loc[i]).values
    L1_Mod=(gene_data['Mod'].loc[i]).values
    L1_Inc=(gene_data['Inc'].loc[i]).values
    L1_Sev=(gene_data['Sev'].loc[i]).values
    L2_Con = (gene_data['Con'].loc['209265_s_at']).values
    L2_Mod = (gene_data['Mod'].loc['209265_s_at']).values
    L2_Inc = (gene_data['Inc'].loc['209265_s_at']).values
    L2_Sev = (gene_data['Sev'].loc['209265_s_at']).values
    res_Con = scipy.stats.pearsonr(L1_Con,L2_Con)[0]
    res_Mod = scipy.stats.pearsonr(L1_Mod, L2_Mod)[0]
    res_Inc = scipy.stats.pearsonr(L1_Inc,L2_Inc)[0]
    res_Sev = scipy.stats.pearsonr(L1_Sev,L2_Sev)[0]
    res_cos = [i, res_Con, res_Mod, res_Inc, res_Sev]
    result_spear.append(res_cos)
# 加载工作簿：
wb = openpyxl.load_workbook(file_path)
sheet1=wb['Sheet2']
for j in result_spear:
    print(j)
    sheet1.append(j)
wb.save(file_path)
wb.close()