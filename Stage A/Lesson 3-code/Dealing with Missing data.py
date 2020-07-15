df_dict2 = {'Name': ['James', 'Yemen', 'Caro', np.nan],
           'Profession': ['Researcher', 'Artist', 'Doctor', 'Writer'],
           'Experience': [12, np.nan, 10, 8],
           'Height': [np.nan, 175, 180, 150]}

new_df = pd.DataFrame(df_dict2)

       Name	Profession	Experience	Height
0	James	Researcher	  12.0	       NaN
1	Yemen	Artist	         NaN	      175.0
2	Caro	Doctor	         10.0	      180.0
3	NaN	Writer	          8.0	      150.0

# check for cells with missing values as True
new_df.isnull()

       Name	Profession	Experience	Height
0	False	  False	  False	True
1	False	  False	  True	       False
2	False	  False	  False	False
3	True	  False	  False	False

# remove rows with missing values
new_df.dropna()
	Name	Profession	Experience	Height
2	Caro	Doctor	         10.0	       180.0
