import pandas as pd
#import matplotlib.pyplot as plt
#from matplotlib import style
#style.use('ggplot')
import numpy as np

web_stats= {'Day':[1,2,3,4,5,6],
            'Visitors':[43,53,34,45,64,34],
            'Bounce_Rate':[65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)      
df=df.set_index('Day')               #df.set_index('Day', inplace=True) no need to change value in original variable.

print(df.head())


#print(df['Bounce_Rate'])
#print(df.Visitors)
#print(df[['Bounce_Rate','Visitors']])

print(df.Visitors.tolist())         #to print in list

#print(df[['Bounce_Rate','Visitors']].tolist())          #error
print(np.array(df[['Bounce_Rate','Visitors']]))
df2=pd.DataFrame(np.array(df[['Bounce_Rate','Visitors']]))
print(df2)

