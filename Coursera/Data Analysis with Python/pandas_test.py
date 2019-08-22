import pandas as pd, timeit

headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
#path = "C:\Users\vicuyzb\source\repos\python_stuff\Coursera\Data Analysis with Python"

start = timeit.timeit()
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header = None)    #read_csv, read_json, read_excel, read_sql
df.columns = headers
#print(df.head(5))  #head/tail
#df.to_csv(path)    #to_csv, to_json, to_excel, to_sql
#print(df.dtypes)
#df.dropna(subset=["normalized-losses"], axis = 0, inplace = True)
print(len(df))
print(df["normalized-losses"].describe(include="all"))
end = timeit.timeit()
print(f"Time spent: {(end - start)*600} seconds")
