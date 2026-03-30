from market_utils import load_dataframe_from_csv, summarize_ma_strategy_with_cost

file_path = "data/aapl_sample.csv"
df = load_dataframe_from_csv(file_path)

split_idx = int(len(df) * 0.7)
train_df = df.iloc[:split_idx].copy()
test_df = df.iloc[split_idx:].copy()

# 假设这是你在训练集挑出来的最佳参数
best_short_window = 3
best_long_window = 5

train_result = summarize_ma_strategy_with_cost(
    train_df.copy(),
    short_window=best_short_window,
    long_window=best_long_window,
    cost_rate=0.001,
)

test_result = summarize_ma_strategy_with_cost(
    test_df.copy(),
    short_window=best_short_window,
    long_window=best_long_window,
    cost_rate=0.001,
)

print("=== Week 2 Day 5 训练集 vs 测试集验证 ===")

print("\n训练集表现:")
print("参数:", (best_short_window, best_long_window))
print("市场收益(%):", round(train_result["market_return_pct"], 2))
print("策略收益(%，未扣成本):", round(train_result["strategy_return_pct"], 2))
print("策略收益(%，扣成本后):", round(train_result["strategy_return_after_cost_pct"], 2))

print("\n测试集表现:")
print("参数:", (best_short_window, best_long_window))
print("市场收益(%):", round(test_result["market_return_pct"], 2))
print("策略收益(%，未扣成本):", round(test_result["strategy_return_pct"], 2))
print("策略收益(%，扣成本后):", round(test_result["strategy_return_after_cost_pct"], 2))