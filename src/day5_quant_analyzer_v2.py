from market_utils import (
    load_dataframe_from_csv,
    add_basic_features,
    get_latest_signal,
    analyze_prices,
)

ticker = "AAPL"
market = "US"
file_path = "data/aapl_sample.csv"

df = load_dataframe_from_csv(file_path)
df = add_basic_features(df)

prices = df["close"].tolist()
result = analyze_prices(prices)
latest_signal = get_latest_signal(df)

print("=== Day 5 迷你量化分析器 V2 ===")
print("股票代码:", ticker)
print("市场:", market)
print("文件路径:", file_path)

print("\n=== 带特征的数据表 ===")
print(df)

print("\n=== 统计结果 ===")
print("上涨天数:", result["up_days"])
print("下跌天数:", result["down_days"])
print("平盘天数:", result["flat_days"])
print("累计收益率:", round(result["total_return"], 4))
print("累计收益率(%):", round(result["total_return"] * 100, 2))
print("最高价:", result["highest_price"])
print("最低价:", result["lowest_price"])
print("平均价格:", round(result["average_price"], 2))
print("趋势判断:", result["trend_label"])
print("波动判断:", result["volatility_label"])

print("\n=== 最新交易观察 ===")
print("最新收盘价:", df.iloc[-1]["close"])
print("最新 3 日均线:", round(df.iloc[-1]["ma_3"], 2))
print("最新 5 日均线:", round(df.iloc[-1]["ma_5"], 2))
print("均线信号:", latest_signal)