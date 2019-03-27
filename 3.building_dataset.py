import quandl
import pandas as pd

#api_key = "VBw65nuv7uNv1JneK3ef"                                                               #api key of quandl
#
#df = quandl.get('FMAC/HPI_AK', authtoken=api_key)                                              #getting df using api_key
#
#print(df.head())                                                                               #printing 5lines of df

fiddy_states = pd.read_html('https://simple.wikipedia.org//wiki/List_of_U.S._states')           #getting abbreivation list

#this is a list:
#print(fiddy_states)                                                                            #printing abbreviation list

#this is a dataframe:
#print(fiddy_states[0])                                                                                         

#this is a column:
#print(fiddy_states[0][0])


for abbr in fiddy_states[0][0][1:]:
    print("FMAC/HPI_"+str(abbr))                                                                #making df code for diffenent places


