from market_utils import (
    get_total_return,
    get_average_price,
    get_highest_price,
    get_lowest_price,
    count_up_down_flat_days,
    get_price_range,
    get_trend_label,
    get_volatility_label,
)

ticker = "AAPL"
market = "US"
prices = [210, 212, 208, 215, 218, 216, 220]

first_price = prices[0]
last_price = prices[-1]

total_return = get_total_return(first_price, last_price)
average_price = get_average_price(prices)
highest_price = get_highest_price(prices)
lowest_price = get_lowest_price(prices)
up_days, down_days, flat_days = count_up_down_flat_days(prices)
price_range = get_price_range(prices)
trend_label = get_trend_label(total_return)
volatility_label = get_volatility_label(price_range)

print("=== Day 3 市场报告 ===")
print("股票代码:", ticker)
print("市场:", market)
print("价格序列:", prices)

print("\n=== 统计结果 ===")
print("上涨天数:", up_days)
print("下跌天数:", down_days)
print("平盘天数:", flat_days)
print("初始价格:", first_price)
print("最终价格:", last_price)
print("累计收益率:", round(total_return, 4))
print("累计收益率(%):", round(total_return * 100, 2))
print("最高价:", highest_price)
print("最低价:", lowest_price)
print("平均价格:", round(average_price, 2))
print("价格区间:", price_range)
print("趋势判断:", trend_label)
print("波动判断:", volatility_label)