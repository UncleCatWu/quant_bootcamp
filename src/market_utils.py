# 累计总收益率 = (最后价格 / 第一个价格) - 1
def get_total_return(first_price, last_price):
    return (last_price / first_price) - 1

# 平均价格 = 价格列表的总和 / 价格列表的长度
def get_average_price(prices):
    return sum(prices) / len(prices)

# 最高价
def get_highest_price(prices):
    return max(prices)

# 最低价
def get_lowest_price(prices):
    return min(prices)

def count_up_down_flat_days(prices):
    up_days = 0
    down_days = 0
    flat_days = 0

    for i in range(1, len(prices)):
        prev_price = prices[i - 1]
        current_price = prices[i]

        if current_price > prev_price:
            up_days += 1
        elif current_price < prev_price:
            down_days += 1
        else:
            flat_days += 1

    return up_days, down_days, flat_days


def get_price_range(prices):
    return max(prices) - min(prices)


def get_trend_label(total_return):
    if total_return > 0:
        return "这段时间整体上涨"
    elif total_return < 0:
        return "这段时间整体下跌"
    else:
        return "这段时间整体平盘"


def get_volatility_label(price_range):
    if price_range >= 10:
        return "波动较大"
    else:
        return "波动较小"
    
def analyze_prices(prices):
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

    return {
        "first_price": first_price,
        "last_price": last_price,
        "total_return": total_return,
        "average_price": average_price,
        "highest_price": highest_price,
        "lowest_price": lowest_price,
        "up_days": up_days,
        "down_days": down_days,
        "flat_days": flat_days,
        "price_range": price_range,
        "trend_label": trend_label,
        "volatility_label": volatility_label,
    }