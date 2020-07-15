# select the row in the at index 3
df.iloc[3] =  Country       Togo
              Capital       Lome
              Population   12000
              Age           75
              Name: 8, dtype: object
# select row with index label 6
df.loc[6] =   Country      Nigeria
              Capital      Abuja
              Population  35000
              Age          80
              Name: 6, dtype: object
# select the Capital column
df['Capital'] = 2      Accra
                4    Nairobi
                6      Abuja
                8       Lome
               Name: Capital, dtype: object
df.at[6, 'Country'] = Nigeria
df.iat[2, 0] = Nigeria
