import pandas as pd
from market_utils import load_dataframe_from_csv, summarize_ma_strategy_with_cost

file_path = "data/aapl_sample.csv"
cost_rate = 0.001

rows = []

for short_window in range(2, 6):
    for long_window in range(4, 11):
        if short_window < long_window:
            df = load_dataframe_from_csv(file_path)
            result = summarize_ma_strategy_with_cost(
                df,
                short_window=short_window,
                long_window=long_window,
                cost_rate=cost_rate,
            )
            rows.append(result)

result_df = pd.DataFrame(rows)
result_df["market_return_pct"] = result_df["market_return_pct"].round(2)
result_df["strategy_return_pct"] = result_df["strategy_return_pct"].round(2)
result_df["strategy_return_after_cost_pct"] = result_df["strategy_return_after_cost_pct"].round(2)

result_df = result_df.sort_values(by="strategy_return_after_cost_pct", ascending=False)

print("=== Week 2 Day 4 参数网格扫描 ===")
print(result_df)