from market_utils import load_prices_from_csv, analyze_prices

stocks = [
    {"ticker": "AAPL", "market": "US", "file_path": "data/aapl_sample.csv"},
    {"ticker": "TSLA", "market": "US", "file_path": "data/tsla_sample.csv"},
]

for stock in stocks:
    ticker = stock["ticker"]
    market = stock["market"]
    file_path = stock["file_path"]

    prices = load_prices_from_csv(file_path)
    result = analyze_prices(prices)

    print("\n==============================")
    print("股票代码:", ticker)
    print("市场:", market)
    print("文件路径:", file_path)
    print("价格序列:", prices)

    print("\n统计结果:")
    print("上涨天数:", result["up_days"])
    print("下跌天数:", result["down_days"])
    print("平盘天数:", result["flat_days"])
    print("累计收益率(%):", round(result["total_return"] * 100, 2))
    print("最高价:", result["highest_price"])
    print("最低价:", result["lowest_price"])
    print("平均价格:", round(result["average_price"], 2))
    print("趋势判断:", result["trend_label"])
    print("波动判断:", result["volatility_label"])