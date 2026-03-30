import pandas as pd
from market_utils import load_dataframe_from_csv, summarize_ma_strategy_with_cost

file_path = "data/aapl_sample.csv"
df = load_dataframe_from_csv(file_path)

split_idx = int(len(df) * 0.7)
train_df = df.iloc[:split_idx].copy()

param_pairs = [
    (2, 4),
    (3, 5),
    (3, 6),
    (4, 8),
    (5, 10),
]

rows = []

for short_window, long_window in param_pairs:
    result = summarize_ma_strategy_with_cost(
        train_df.copy(),
        short_window=short_window,
        long_window=long_window,
        cost_rate=0.001,
    )
    rows.append(result)

result_df = pd.DataFrame(rows)
result_df["market_return_pct"] = result_df["market_return_pct"].round(2)
result_df["strategy_return_pct"] = result_df["strategy_return_pct"].round(2)
result_df["strategy_return_after_cost_pct"] = result_df["strategy_return_after_cost_pct"].round(2)

result_df = result_df.sort_values(by="strategy_return_after_cost_pct", ascending=False)

print("=== Week 2 Day 5 训练集参数选择 ===")
print(result_df)