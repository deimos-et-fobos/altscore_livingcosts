import pandas as pd

train = pd.read_csv("./data/train.csv")
test = pd.read_csv("./data/test.csv")
mobility = pd.read_parquet("./data/mobility_data.parquet")

print(train)