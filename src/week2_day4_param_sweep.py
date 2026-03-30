import pandas as pd
from market_utils import load_dataframe_from_csv, build_ma_strategy_dataframe_with_cost

file_path = "data/aapl_sample.csv"
cost_rate = 0.001

param_pairs = [
    (2, 4),
    (3, 5),
    (3, 6),
    (4, 8),
    (5, 10),
]

rows = []

for short_window, long_window in param_pairs:
    df = load_dataframe_from_csv(file_path)
    df = build_ma_strategy_dataframe_with_cost(
        df,
        short_window=short_window,
        long_window=long_window,
        cost_rate=cost_rate,
    )

    market_final = df["cum_return"].dropna().iloc[-1]
    strategy_final = df["strategy_cum_return"].dropna().iloc[-1]
    strategy_after_cost_final = df["strategy_cum_return_after_cost"].dropna().iloc[-1]

    row = {
        "short_window": short_window,
        "long_window": long_window,
        "market_return_pct": round((market_final - 1) * 100, 2),
        "strategy_return_pct": round((strategy_final - 1) * 100, 2),
        "strategy_return_after_cost_pct": round((strategy_after_cost_final - 1) * 100, 2),
    }
    rows.append(row)

result_df = pd.DataFrame(rows)
result_df = result_df.sort_values(by="strategy_return_after_cost_pct", ascending=False)

print("=== Week 2 Day 4 参数扫描结果 ===")
print(result_df)