import pandas as pd
from market_utils import analyze_prices

ticker = "AAPL"
market = "US"
file_path = "data/aapl_sample.csv"

df = pd.read_csv(file_path)
prices = df["close"].tolist()

result = analyze_prices(prices)

print("=== Day 4 从 CSV 生成市场报告 ===")
print("股票代码:", ticker)
print("市场:", market)
print("文件路径:", file_path)
print("价格序列:", prices)

print("\n=== 统计结果 ===")
print("上涨天数:", result["up_days"])
print("下跌天数:", result["down_days"])
print("平盘天数:", result["flat_days"])
print("初始价格:", result["first_price"])
print("最终价格:", result["last_price"])
print("累计收益率:", round(result["total_return"], 4))
print("累计收益率(%):", round(result["total_return"] * 100, 2))
print("最高价:", result["highest_price"])
print("最低价:", result["lowest_price"])
print("平均价格:", round(result["average_price"], 2))
print("价格区间:", result["price_range"])
print("趋势判断:", result["trend_label"])
print("波动判断:", result["volatility_label"])