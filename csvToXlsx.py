import pandas as pd

df_new = pd.read_csv('extract.csv')
writer = pd.ExcelWriter('incidents.xlsx')
df_new.to_excel(writer, index = False)
writer.save()
