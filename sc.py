import openpyxl
import pandas as pd


def add_w(a, b):
    a = abs(a)
    b = abs(b)
    return a * (a / (a + b)) + b * (b / (a + b))


file_path = r'.\\dataset\\AD病标准化数据.xlsx'  # r对路径进行转义，windows需要
gene_order = pd.read_excel(file_path, sheet_name=['Sheet1', 'Sheet2'], header=0)
id = (gene_order['Sheet2'].iloc[:, 0:1]).values
con_x1_1 = (gene_order['Sheet1'].iloc[:, 1:2]).values
mod_x2_1 = (gene_order['Sheet1'].iloc[:, 2:3]).values
inc_x3_1 = (gene_order['Sheet1'].iloc[:, 3:4]).values
sev_x4_1 = (gene_order['Sheet1'].iloc[:, 4:5]).values

con_x1_2 = (gene_order['Sheet2'].iloc[:, 1:2]).values
mod_x2_2 = (gene_order['Sheet2'].iloc[:, 2:3]).values
inc_x3_2 = (gene_order['Sheet2'].iloc[:, 3:4]).values
sev_x4_2 = (gene_order['Sheet2'].iloc[:, 4:5]).values

x1 = []
for i in range(len(id)):
    x1.append([id[i][0], add_w(con_x1_1[i][0], con_x1_2[i][0]), add_w(mod_x2_1[i][0], mod_x2_2[i][0]),
               add_w(inc_x3_1[i][0], inc_x3_2[i][0]), add_w(sev_x4_1[i][0], sev_x4_2[i][0])])
print(x1)
wb = openpyxl.load_workbook(file_path)
sheet1 = wb['Sheet3']
for j in x1:
    sheet1.append(j)
print('正在保存...')
wb.save(file_path)
wb.close()
