import pandas as pd


df = pd.read_csv('/home/kushagra/Downloads/ZILLOW-Z77006_ZRIMFRR.csv')
df.set_index('Date', inplace=True)
print(df.head())

#df.to_csv('newcsv2.csv')         #saving to csv


df=pd.read_csv('newcsv2.csv', index_col=0)          #inbuild feature to set index 
print(df.head())

df.columns = ['Austin_HPI']
print(df.head())


#df.to_csv('newcsv3.csv' , header=False)            #no header in output file

#df = pd.read_csv('newcsv4.csv', names=['Date','Austin_HPI'], index_col=0)              #giving headernames

