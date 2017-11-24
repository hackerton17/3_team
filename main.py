import pandas

# data = pandas.read_csv('')
data_Branches = pandas.read_excel('case1/Materials for local case/Customer codes.xlsx', sheetname='Branches')
data_Customers = pandas.read_excel('case1/Materials for local case/Customer codes.xlsx', sheetname='Customers')
print(data_Branches)
print(data_Customers)