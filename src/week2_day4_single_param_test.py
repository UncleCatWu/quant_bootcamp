from market_utils import load_dataframe_from_csv, build_ma_strategy_dataframe_with_cost

file_path = "data/aapl_sample.csv"
short_window = 3
long_window = 5
cost_rate = 0.001

df = load_dataframe_from_csv(file_path)
df = build_ma_strategy_dataframe_with_cost(
    df,
    short_window=short_window,
    long_window=long_window,
    cost_rate=cost_rate,
)

print(f"=== 参数测试: MA{short_window} / MA{long_window} ===")
print(df)