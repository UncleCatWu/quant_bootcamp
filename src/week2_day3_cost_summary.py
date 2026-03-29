from market_utils import load_dataframe_from_csv, build_strategy_dataframe_with_cost

file_path = "data/aapl_sample.csv"
df = load_dataframe_from_csv(file_path)
df = build_strategy_dataframe_with_cost(df, cost_rate=0.001)

market_final = df["cum_return"].dropna().iloc[-1]
strategy_final = df["strategy_cum_return"].dropna().iloc[-1]
strategy_after_cost_final = df["strategy_cum_return_after_cost"].dropna().iloc[-1]

print("=== Week 2 Day 3 成本影响总结 ===")
print("市场最终净值:", round(market_final, 4))
print("策略最终净值（未扣成本）:", round(strategy_final, 4))
print("策略最终净值（扣成本后）:", round(strategy_after_cost_final, 4))

print("市场总收益(%):", round((market_final - 1) * 100, 2))
print("策略总收益(%，未扣成本):", round((strategy_final - 1) * 100, 2))
print("策略总收益(%，扣成本后):", round((strategy_after_cost_final - 1) * 100, 2))