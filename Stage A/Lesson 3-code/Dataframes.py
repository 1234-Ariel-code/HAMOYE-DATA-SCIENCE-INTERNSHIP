
print(pd.DataFrame())
# prints an empty dataframe
Empty DataFrame
Columns: []
Index: []

# create a dataframe from a dictionary
df_dict = {'Country': ['Ghana', 'Kenya', 'Nigeria', 'Togo'],
           'Capital': ['Accra', 'Nairobi', 'Abuja', 'Lome'],
           'Population': [10000, 8500, 35000, 12000],
           'Age': [60, 70, 80, 75]
}
df = pd.DataFrame(df_dict, index=[2, 4, 6, 8])

df_list = [['Ghana', 'Accra', 10000, 60], 
           ['Kenya', 'Nairobi', 8500, 70], 
           ['Nigeria',   'Abuja', 35000, 80], 
           ['Togo', 'Lome', 12000, 75]]
df1 = pd.DataFrame(df_list, columns=['Country', 'Capital','Population', 'Age'], 
                   index=[2, 4, 6, 8])

# df and df1 prints this
      Country   Capital   Population	Age
2	Ghana	     Accra     10000	60
4	Kenya	     Nairobi   8500	       70
6	Nigeria     Abuja     35000	80
8	Togo	     Lome      12000	75