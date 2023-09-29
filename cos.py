import openpyxl
import pandas as pd
import numpy as np


def get_cos_similar(v1: list, v2: list):
    num = float(np.dot(v1, v2))  # 向量点乘
    denom = np.linalg.norm(v1) * np.linalg.norm(v2)  # 求模长的乘积
    return (num / denom) if denom != 0 else 0


file_path = r'.\\dataset\\AD病标准化数据.xlsx'  # r对路径进行转义，windows需要
gene_data = pd.read_excel(file_path, sheet_name=['Con', 'Mod', 'Inc', 'Sev'], header=1, index_col=0)
# cmp=['209265_s_at',0.653781261584486,0.703498319596823,0.67079205355854,0.606279622329254,0.77785616530607,0.71979568618531,0.681408727145721,0.689221035085699,0.760686854810633]
List_1 = gene_data['Con'].values
result_cos = []
for i in gene_data['Con'].index:
    # print((gene_data['Con'].loc[i]).values)
    L1_Con = (gene_data['Con'].loc[i]).values
    L1_Mod = (gene_data['Mod'].loc[i]).values
    L1_Inc = (gene_data['Inc'].loc[i]).values
    L1_Sev = (gene_data['Sev'].loc[i]).values
    L2_Con = (gene_data['Con'].loc['209265_s_at']).values
    L2_Mod = (gene_data['Mod'].loc['209265_s_at']).values
    L2_Inc = (gene_data['Inc'].loc['209265_s_at']).values
    L2_Sev = (gene_data['Sev'].loc['209265_s_at']).values
    res_Con = get_cos_similar(L1_Con, L2_Con)
    res_Mod = get_cos_similar(L1_Mod, L2_Mod)
    res_Inc = get_cos_similar(L1_Inc, L2_Inc)
    res_Sev = get_cos_similar(L1_Sev, L2_Sev)
    res_cos = [i, res_Con, res_Mod, res_Inc, res_Sev]
    result_cos.append(res_cos)
# print(result_cos)
# 加载工作簿：
wb = openpyxl.load_workbook(file_path)
sheet1 = wb['Sheet1']
for j in result_cos:
    print(j)
    sheet1.append(j)
wb.save(file_path)
wb.close()
