import pandas as pd

file_path = "data/aapl_sample.csv"
df = pd.read_csv(file_path)

# 1. 计算基础特征
df["return"] = df["close"].pct_change()
df["ma_3"] = df["close"].rolling(3).mean()
df["ma_5"] = df["close"].rolling(5).mean()

# 2. 生成信号列
df["signal"] = 0
df.loc[df["ma_3"] > df["ma_5"], "signal"] = 1

# 3. 生成持仓列
df["position"] = df["signal"].shift(1)

# 4. 计算策略收益
df["strategy_return"] = df["position"] * df["return"]

# 5. 计算净值
df["cum_return"] = (1 + df["return"]).cumprod()
df["strategy_cum_return"] = (1 + df["strategy_return"]).cumprod()

print(df)