import pandas as pd
url = 'https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv?raw=true'
df = pd.read_csv(url,index_col=0)

print(df.head(5))