import pandas

# data = pandas.read_csv('')
data_Branches = pandas.read_excel('case1/Materials for local case/Customer codes.xlsx', sheetname='Branches')
data_Customers = pandas.read_excel('case1/Materials for local case/Customer codes.xlsx', sheetname='Customers')
print(data_Branches)
print(data_Customers)

data = pandas.read_csv('case1/Materials for local case/pg-recommender/data/data.csv')
print(data)

data_op = pandas.read_csv('case1/Materials for local case/pg-recommender/data/op_src_parameters.csv')
print(data_op)

data_EE = pandas.read_csv('case1/Materials for local case/Transactions data/EEAPT_IS_Monthly_20170430.csv', names=['SRCE_SYS_ID','FACT_TYPE_CODE','SBMSN_TYPE_CODE','DUE_PERD','Code of the time period during which transaction took place','Transaction date','CUST_ID','PROD_ID','GEO_ID','To be left null','To be left null','To be left null','SCNDR_SHIP_FLAG','To be left null','Currency of transaction','Coverage','To be left null','To be left null','To be left null','To be left null','Constant','DIST_ID','Constant','Distributor group code','To be left null','To be felt null','To be left null','Pack level in which transaction took place','NIV','Business Interface value','Volume (quantity)','GIV'])
print(data_EE)

data_CMD = pandas.read_csv('case1/Materials for local case/Customers Master Data.csv')
print(data_CMD)


print(data_EE.groupby('LGCY_STORE_ID'))