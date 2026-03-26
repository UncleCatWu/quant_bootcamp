from market_utils import load_dataframe_from_csv, build_strategy_dataframe

file_path = "data/aapl_sample.csv"

df = load_dataframe_from_csv(file_path)
df = build_strategy_dataframe(df)

print("=== Week 2 Day 1 策略研究表 ===")
print(df)