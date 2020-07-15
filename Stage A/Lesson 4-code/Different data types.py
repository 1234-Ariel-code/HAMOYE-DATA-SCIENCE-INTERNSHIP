
csv_df = pd.read_csv('sample_file.csv')
csv_df.to_csv('sample_file.csv', index=False)

#sometimes dependent on the xlrd library which can be installed by running pip install xlrd in the terminal
excel_df = pd.read_excel('sample_file.xlsx')
excel_df.to_excel('sample_file.xlsx')

#read table from a webpage and save as a dataframe
html_df = pd.read_html('http://www.webpage.com/sampledata.html')
html_df.to_html('sample_file.html')
