import pandas as pd
from market_utils import load_dataframe_from_csv, summarize_ma_strategy_with_cost

file_path = "data/aapl_sample.csv"
df = load_dataframe_from_csv(file_path)

split_idx = int(len(df) * 0.7)
train_df = df.iloc[:split_idx].copy()
test_df = df.iloc[split_idx:].copy()

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

train_result_df = pd.DataFrame(rows)
train_result_df = train_result_df.sort_values(
    by="strategy_return_after_cost_pct",
    ascending=False,
)

best_row = train_result_df.iloc[0]
best_short_window = int(best_row["short_window"])
best_long_window = int(best_row["long_window"])

test_result = summarize_ma_strategy_with_cost(
    test_df.copy(),
    short_window=best_short_window,
    long_window=best_long_window,
    cost_rate=0.001,
)

print("=== Week 2 Day 5 训练-测试流程 ===")
print("训练集最优参数:", (best_short_window, best_long_window))

print("\n训练集最优结果:")
print("市场收益(%):", round(best_row["market_return_pct"], 2))
print("策略收益(%，未扣成本):", round(best_row["strategy_return_pct"], 2))
print("策略收益(%，扣成本后):", round(best_row["strategy_return_after_cost_pct"], 2))

print("\n测试集验证结果:")
print("市场收益(%):", round(test_result["market_return_pct"], 2))
print("策略收益(%，未扣成本):", round(test_result["strategy_return_pct"], 2))
print("策略收益(%，扣成本后):", round(test_result["strategy_return_after_cost_pct"], 2))