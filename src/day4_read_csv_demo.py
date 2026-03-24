import pandas as pd

df = pd.read_csv("data/aapl_sample.csv")

print("=== 原始数据 ===")
print(df)

print("\n=== close 列 ===")
print(df["close"])

prices = df["close"].tolist()

print("\n=== 转成列表后的价格序列 ===")
print(prices)