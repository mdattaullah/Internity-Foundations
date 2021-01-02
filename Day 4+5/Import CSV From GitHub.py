import pandas as pd
url = 'https://raw.githubusercontent.com/rjrealworld/Internity-Foundations/main/Day%204%2B5/Intra-StateWarData_v4.1.csv'
df = pd.read_csv(url,index_col=0, encoding='latin-1')

print(df.head(5))
