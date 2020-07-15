# convention for importing numpy
import pandas as pd
days = pd.Series(['Monday', 'Tuesday', 'Wednesday'])
print(days) # prints
0       Monday
1      Tuesday
2    Wednesday
dtype: object
# creating series with a numpy array
days_list = np.array(['Monday', 'Tuesday', 'Wednesday'])
numpy_days = pd.Series(days_list)
print(numpy_days) # prints
0       Monday
1      Tuesday
2    Wednesday
dtype: object

# using strings as index
days = pd.Series(['Monday', 'Tuesday', 'Wednesday'], 
 index=['a', 'b', 'c'])
# create series from a dictionary
days1 = pd.Series({'a':'Monday', 'b':'Tuesday', 'c':'Wednesday'})

# days and days1 prints this 
a       Monday
b      Tuesday
c    Wednesday
dtype: object

#Series can be accessed using the specified index as shown below
days[0] =  Monday

days[1: ] = b      Tuesday
            c    Wednesday
            dtype: object

days['c']  = Wednesday
