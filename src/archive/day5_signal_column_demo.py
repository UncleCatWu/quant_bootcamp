import pandas as pd

file_path = "data/aapl_sample.csv"
df = pd.read_csv(file_path)

df["return"] = df["close"].pct_change()
df["ma_3"] = df["close"].rolling(3).mean()
df["ma_5"] = df["close"].rolling(5).mean()

df["signal"] = "neutral"
df.loc[df["ma_3"] > df["ma_5"], "signal"] = "bullish"
df.loc[df["ma_3"] < df["ma_5"], "signal"] = "bearish"

print(df)