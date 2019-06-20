import pandas as pd, timeit

start = timeit.timeit()
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header = None)
end = timeit.timeit()
print(f"Time spent: {(end - start)*600} seconds")
