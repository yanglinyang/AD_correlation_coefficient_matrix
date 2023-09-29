import pandas as pd
import openpyxl

file_path = r'.\\dataset\\AD病标准化数据.xlsx'   # r对路径进行转义，windows需要
gene_order = pd.read_excel(file_path, sheet_name=['Sheet3'], header=0)  #读取单元表
id=(gene_order['Sheet3'].iloc[:,0:1]).values
con_x1=(gene_order['Sheet3'].iloc[:,1:2]).values
mod_x2=(gene_order['Sheet3'].iloc[:,2:3]).values
inc_x3=(gene_order['Sheet3'].iloc[:,3:4]).values
sev_x4=(gene_order['Sheet3'].iloc[:,4:5]).values
x1=[]
# print(con_x1)
for i in range(len(con_x1)):
     x1.append([id[i][0],mod_x2[i][0]-con_x1[i][0],inc_x3[i][0]-con_x1[i][0],sev_x4[i][0]-con_x1[i][0]])
wb = openpyxl.load_workbook(file_path)
sheet1=wb['Sheet6']
for j in x1:
    sheet1.append(j)
print('正在保存...')
wb.save(file_path)
wb.close()