import pandas as pd


def load_dataframe_from_csv(file_path):
    return pd.read_csv(file_path)


def load_prices_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df["close"].tolist()


def add_return_column(df):
    df = df.copy()
    df["return"] = df["close"].pct_change()
    return df


def add_moving_average(df, window):
    df = df.copy()
    df[f"ma_{window}"] = df["close"].rolling(window).mean()
    return df


def add_basic_features(df):
    df = add_return_column(df)
    df = add_moving_average(df, 3)
    df = add_moving_average(df, 5)
    return df


def get_total_return(first_price, last_price):
    return (last_price / first_price) - 1


def get_average_price(prices):
    return sum(prices) / len(prices)


def get_highest_price(prices):
    return max(prices)


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
    if len(prices) == 0:
        raise ValueError("prices 不能为空")

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


def get_latest_row(df):
    return df.iloc[-1]


def get_latest_signal(df):
    latest = get_latest_row(df)

    ma_3 = latest["ma_3"]
    ma_5 = latest["ma_5"]

    if pd.isna(ma_3) or pd.isna(ma_5):
        return "均线数据不足"

    if ma_3 > ma_5:
        return "短期偏强"
    elif ma_3 < ma_5:
        return "短期偏弱"
    else:
        return "短期中性"


def analyze_stock_from_csv(ticker, file_path, market="US"):
    df = load_dataframe_from_csv(file_path)
    df = add_basic_features(df)

    prices = df["close"].tolist()
    summary = analyze_prices(prices)
    latest_signal = get_latest_signal(df)

    return {
        "ticker": ticker,
        "market": market,
        "file_path": file_path,
        "dataframe": df,
        "summary": summary,
        "latest_signal": latest_signal,
    }


def build_summary_row(report):
    summary = report["summary"]
    df = report["dataframe"]

    return {
        "ticker": report["ticker"],
        "market": report["market"],
        "latest_close": df.iloc[-1]["close"],
        "return_pct": round(summary["total_return"] * 100, 2),
        "up_days": summary["up_days"],
        "down_days": summary["down_days"],
        "trend": summary["trend_label"],
        "signal": report["latest_signal"],
    }


def print_market_report(report):
    summary = report["summary"]
    df = report["dataframe"]

    print("\n==============================")
    print("股票代码:", report["ticker"])
    print("市场:", report["market"])
    print("文件路径:", report["file_path"])

    print("\n统计结果:")
    print("上涨天数:", summary["up_days"])
    print("下跌天数:", summary["down_days"])
    print("平盘天数:", summary["flat_days"])
    print("累计收益率:", round(summary["total_return"], 4))
    print("累计收益率(%):", round(summary["total_return"] * 100, 2))
    print("最高价:", summary["highest_price"])
    print("最低价:", summary["lowest_price"])
    print("平均价格:", round(summary["average_price"], 2))
    print("趋势判断:", summary["trend_label"])
    print("波动判断:", summary["volatility_label"])

    print("\n最新观察:")
    print("最新收盘价:", df.iloc[-1]["close"])
    print("最新 3 日均线:", round(df.iloc[-1]["ma_3"], 2))
    print("最新 5 日均线:", round(df.iloc[-1]["ma_5"], 2))
    print("均线信号:", report["latest_signal"])