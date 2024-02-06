import pandas as pd

chunk_size = 1000
df = pd.read_csv("../data/orders.txt", chunksize=chunk_size)
for i, chunk in enumerate(df,start=1):
    print(f"Chunk {i}:")