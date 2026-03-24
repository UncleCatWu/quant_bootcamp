prices = [210, 212, 208, 215, 218, 216, 220]

print("=== 迷你行情分析器 ===")
print("价格序列:", prices)

up_days = 0
down_days = 0
flat_days = 0

ticker = "AAPL"
market = "US"
print("股票代码:", ticker)
print("市场:", market)

for i in range(1, len(prices)):
    prev_price = prices[i - 1]
    current_price = prices[i]

    print(f"\n第 {i + 1} 天:")
    print("前一天价格:", prev_price)
    print("当天价格:", current_price)

    if current_price > prev_price:
        print("结果: 上涨")
        up_days += 1
    elif current_price < prev_price:
        print("结果: 下跌")
        down_days += 1
    else:
        print("结果: 平盘")
        flat_days += 1

first_price = prices[0]
last_price = prices[-1]
total_return = (last_price / first_price) - 1
highest_price = max(prices)
lowest_price = min(prices)
average_price = sum(prices) / len(prices)

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
print("平均价格:", average_price)

if total_return > 0:
    print("结论: 这段时间整体上涨")
elif total_return < 0:
    print("结论: 这段时间整体下跌")
else:
    print("结论: 这段时间整体平盘")
    
price_range = highest_price - lowest_price

if price_range >= 10:
    print("波动判断: 波动较大")
else:
    print("波动判断: 波动较小")