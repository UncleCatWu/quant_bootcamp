import pandas as pd

file_path = "data/aapl_sample.csv"
df = pd.read_csv(file_path)

print("=== 原始数据 ===")
print(df)

df["return"] = df["close"].pct_change()
df["ma_3"] = df["close"].rolling(3).mean()
df["ma_5"] = df["close"].rolling(5).mean()

print("\n=== 加入收益率和均线后的数据 ===")
print(df)

print("\n=== 最后 5 行 ===")
print(df.tail())