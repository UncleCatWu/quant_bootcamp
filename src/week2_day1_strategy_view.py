from market_utils import load_dataframe_from_csv, build_strategy_dataframe

file_path = "data/aapl_sample.csv"

df = load_dataframe_from_csv(file_path)
df = build_strategy_dataframe(df)

columns = [
    "date",
    "close",
    "return",
    "ma_3",
    "ma_5",
    "signal",
    "position",
    "strategy_return",
    "cum_return",
    "strategy_cum_return",
]

print("=== Week 2 Day 1 策略关键列 ===")
print(df[columns])