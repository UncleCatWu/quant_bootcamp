from market_utils import load_dataframe_from_csv, build_strategy_dataframe_with_cost

file_path = "data/aapl_sample.csv"
df = load_dataframe_from_csv(file_path)
df = build_strategy_dataframe_with_cost(df, cost_rate=0.001)

columns = [
    "date",
    "close",
    "signal",
    "position",
    "position_change",
    "return",
    "strategy_return",
    "cost",
    "strategy_return_after_cost",
    "cum_return",
    "strategy_cum_return",
    "strategy_cum_return_after_cost",
]

print("=== Week 2 Day 3 含交易成本策略表 ===")
print(df[columns])