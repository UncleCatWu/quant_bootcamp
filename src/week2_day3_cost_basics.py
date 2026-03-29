from market_utils import load_dataframe_from_csv, build_strategy_dataframe

file_path = "data/aapl_sample.csv"
df = load_dataframe_from_csv(file_path)
df = build_strategy_dataframe(df)

# 1. 计算仓位变化
df["position_change"] = df["position"].diff().abs()

# 2. 定义单次交易成本
cost_rate = 0.001  # 0.1%

# 3. 计算成本列
df["cost"] = df["position_change"] * cost_rate

# 4. 计算扣成本后的策略收益
df["strategy_return_after_cost"] = df["strategy_return"] - df["cost"]

# 5. 计算扣成本后的策略净值
df["strategy_cum_return_after_cost"] = (1 + df["strategy_return_after_cost"]).cumprod()

print(df)