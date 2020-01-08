import xlrd

excel = xlrd.open_workbook(u'123.xlsx')

#table = excel.sheets()[0]
#table = excel.sheet_by_index(0)

table = excel.sheet_by_name(u'Sheet1')

print(table)

# 获取行数
nrows = table.nrows

# 获取列数
ncols = table.ncols