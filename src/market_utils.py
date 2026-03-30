import pandas as pd


def load_dataframe_from_csv(file_path):
    """读取指定路径的 CSV 文件并返回 DataFrame。

    适用场景：
        当后续还需要继续对整张表做特征加工、筛选、统计时，优先使用本函数。

    Args:
        file_path (str): CSV 文件路径。

    Returns:
        pandas.DataFrame: 包含 CSV 全部列的数据表。
    """
    return pd.read_csv(file_path)


def load_prices_from_csv(file_path):
    """从 CSV 文件中读取 close 列并转换为 Python 列表。

    适用场景：
        当只关心价格序列，准备把数据交给纯 Python 分析函数时使用。

    Args:
        file_path (str): CSV 文件路径。

    Returns:
        list: 收盘价序列。
    """
    df = pd.read_csv(file_path)
    return df["close"].tolist()


def add_return_column(df):
    """为 DataFrame 增加收益率列 return。

    计算逻辑：
        使用 pandas 的 pct_change() 计算当前行相对上一行的百分比变化。
        第一行由于没有前一行可比较，因此结果会是 NaN。

    Args:
        df (pandas.DataFrame): 原始行情表，必须包含 close 列。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含新增的 return 列。
    """
    df = df.copy()
    df["return"] = df["close"].pct_change()
    return df


def add_moving_average(df, window):
    """为 DataFrame 增加移动平均线列。

    例如当 window=3 时，会新增 ma_3；当 window=5 时，会新增 ma_5。
    前 window-1 行由于数据不足，结果会是 NaN。

    Args:
        df (pandas.DataFrame): 原始行情表，必须包含 close 列。
        window (int): 均线窗口大小，例如 3、5、10。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含新增均线列。
    """
    df = df.copy()
    df[f"ma_{window}"] = df["close"].rolling(window).mean()
    return df


def add_basic_features(df):
    """一次性为 DataFrame 增加最基础的量化特征列。

    当前版本会增加：
        - return: 日收益率
        - ma_3: 3 日均线
        - ma_5: 5 日均线

    Args:
        df (pandas.DataFrame): 原始行情表。

    Returns:
        pandas.DataFrame: 加工后的 DataFrame。
    """
    df = add_return_column(df)
    df = add_moving_average(df, 3)
    df = add_moving_average(df, 5)
    return df


def get_total_return(first_price, last_price):
    """计算累计收益率。

    公式：
        (最后价格 / 初始价格) - 1

    Args:
        first_price (float): 初始价格。
        last_price (float): 最终价格。

    Returns:
        float: 累计收益率。
    """
    return (last_price / first_price) - 1


def get_average_price(prices):
    """计算价格序列的平均价格。

    Args:
        prices (list[float]): 价格列表。

    Returns:
        float: 平均价格。
    """
    return sum(prices) / len(prices)


def get_highest_price(prices):
    """获取价格序列中的最高价。

    Args:
        prices (list[float]): 价格列表。

    Returns:
        float: 序列中的最大值。
    """
    return max(prices)


def get_lowest_price(prices):
    """获取价格序列中的最低价。

    Args:
        prices (list[float]): 价格列表。

    Returns:
        float: 序列中的最小值。
    """
    return min(prices)


def count_up_down_flat_days(prices):
    """统计价格序列中的上涨、下跌和平盘天数。

    计算逻辑：
        从第二个价格开始，与前一天逐一比较。
        - 当前价格 > 前一天价格：上涨天数 +1
        - 当前价格 < 前一天价格：下跌天数 +1
        - 当前价格 == 前一天价格：平盘天数 +1

    Args:
        prices (list[float]): 价格列表。

    Returns:
        tuple[int, int, int]: (up_days, down_days, flat_days)
    """
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
    """计算价格区间，即最高价减去最低价。

    这个值可以粗略衡量该段时间的绝对波动幅度。

    Args:
        prices (list[float]): 价格列表。

    Returns:
        float: 价格区间。
    """
    return max(prices) - min(prices)


def get_trend_label(total_return):
    """根据累计收益率给出趋势文字标签。

    Args:
        total_return (float): 累计收益率。

    Returns:
        str: 趋势描述。
    """
    if total_return > 0:
        return "这段时间整体上涨"
    elif total_return < 0:
        return "这段时间整体下跌"
    else:
        return "这段时间整体平盘"


def get_volatility_label(price_range):
    """根据价格区间给出粗略的波动标签。

    当前规则：
        - price_range >= 10: 波动较大
        - 其他情况: 波动较小

    Args:
        price_range (float): 价格区间。

    Returns:
        str: 波动描述。
    """
    if price_range >= 10:
        return "波动较大"
    else:
        return "波动较小"


def analyze_prices(prices):
    """对价格序列做综合分析并返回结构化结果。

    统一调用前面已经封装好的小函数，输出：
        - 起始价格、结束价格
        - 累计收益率
        - 平均价格
        - 最高价、最低价
        - 上涨/下跌/平盘天数
        - 价格区间
        - 趋势标签
        - 波动标签

    Args:
        prices (list[float]): 价格列表，不能为空。

    Raises:
        ValueError: 当 prices 为空时抛出。

    Returns:
        dict: 完整分析结果字典。
    """
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
    """获取 DataFrame 的最后一行。

    常用于读取最新一天的行情数据或最新特征值。

    Args:
        df (pandas.DataFrame): 数据表。

    Returns:
        pandas.Series: 最后一行数据。
    """
    return df.iloc[-1]


def get_latest_signal(df):
    """根据最新一行的短周期均线和长周期均线生成简单信号。

    当前规则：
        - ma_3 > ma_5: 短期偏强
        - ma_3 < ma_5: 短期偏弱
        - ma_3 == ma_5: 短期中性
        - 若均线数据缺失: 均线数据不足

    Args:
        df (pandas.DataFrame): 已包含 ma_3 和 ma_5 列的数据表。

    Returns:
        str: 均线信号描述。
    """
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
    """从单只股票的 CSV 文件出发，完成整条分析链路。

    执行步骤：
        1. 读取 CSV 为 DataFrame
        2. 增加基础特征列
        3. 提取 close 价格序列
        4. 对价格序列做统计分析
        5. 计算最新均线信号
        6. 返回完整报告字典

    Args:
        ticker (str): 股票代码，例如 AAPL、TSLA、CATL。
        file_path (str): 对应 CSV 文件路径。
        market (str, optional): 市场代码，默认值为 "US"。

    Returns:
        dict: 包含股票基本信息、DataFrame、统计摘要和最新信号的报告。
    """
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
    """把完整报告压缩为一行摘要数据，便于构建汇总表。

    适用场景：
        当批量分析多只股票后，需要生成横向比较的 DataFrame 总表。

    Args:
        report (dict): analyze_stock_from_csv 返回的完整报告字典。

    Returns:
        dict: 一行摘要数据。
    """
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
    """打印单只股票的完整市场报告。

    这个函数负责把结构化结果格式化输出到终端，便于人工阅读。

    Args:
        report (dict): analyze_stock_from_csv 返回的完整报告字典。

    Returns:
        None: 仅执行打印，不返回值。
    """
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
    
def add_signal_column(df):
    """根据 ma_3 和 ma_5 生成基础信号列。

    规则：
        - 当 ma_3 > ma_5 时，signal = 1
        - 其他情况，signal = 0

    Args:
        df (pandas.DataFrame): 已包含 ma_3 和 ma_5 列的数据表。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含 signal 列。
    """
    df = df.copy()
    df["signal"] = 0
    df.loc[df["ma_3"] > df["ma_5"], "signal"] = 1
    return df

def add_position_column(df):
    """根据信号列生成持仓列。

    规则：
        使用前一天的 signal 作为今天的实际持仓，
        以避免使用未来信息。

    Args:
        df (pandas.DataFrame): 已包含 signal 列的数据表。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含 position 列。
    """
    df = df.copy()
    df["position"] = df["signal"].shift(1)
    return df

def add_strategy_return_column(df):
    """根据持仓列和市场收益率列生成策略收益列。

    规则：
        strategy_return = position * return

    Args:
        df (pandas.DataFrame): 已包含 position 和 return 列的数据表。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含 strategy_return 列。
    """
    df = df.copy()
    df["strategy_return"] = df["position"] * df["return"]
    return df

def add_cumulative_return_columns(df):
    """增加市场净值列和策略净值列。

    新增列：
        - cum_return: 市场买入持有净值
        - strategy_cum_return: 策略累计净值

    Args:
        df (pandas.DataFrame): 已包含 return 和 strategy_return 列的数据表。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含累计净值列。
    """
    df = df.copy()
    df["cum_return"] = (1 + df["return"]).cumprod()
    df["strategy_cum_return"] = (1 + df["strategy_return"]).cumprod()
    return df

def build_strategy_dataframe(df):
    """基于价格数据构建最基础的策略研究表。

    执行步骤：
        1. 增加 return、ma_3、ma_5
        2. 生成 signal
        3. 生成 position
        4. 生成 strategy_return
        5. 生成累计净值列

    Args:
        df (pandas.DataFrame): 原始行情表，至少包含 close 列。

    Returns:
        pandas.DataFrame: 包含特征、信号、持仓、收益、净值的完整策略表。
    """
    df = add_basic_features(df)
    df = add_signal_column(df)
    df = add_position_column(df)
    df = add_strategy_return_column(df)
    df = add_cumulative_return_columns(df)
    return df

def get_total_market_return(df):
    """获取市场总收益。

    Args:
        df (pandas.DataFrame): 已包含 cum_return 列的数据表。

    Returns:
        float: 市场总收益率。
    """
    return df["cum_return"].iloc[-1] - 1

def get_total_strategy_return(df):
    """获取策略总收益。

    Args:
        df (pandas.DataFrame): 已包含 strategy_cum_return 列的数据表。

    Returns:
        float: 策略总收益率。
    """
    return df["strategy_cum_return"].iloc[-1] - 1

def get_strategy_win_rate(df):
    """计算策略日胜率。

    这里先按 strategy_return > 0 的天数占有效策略收益天数的比例计算。

    Args:
        df (pandas.DataFrame): 已包含 strategy_return 列的数据表。

    Returns:
        float: 胜率；如果没有有效交易日，则返回 0。
    """
    strategy_returns = df["strategy_return"].dropna()
    strategy_returns = strategy_returns[strategy_returns != 0]

    if len(strategy_returns) == 0:
        return 0

    win_days = (strategy_returns > 0).sum()
    return win_days / len(strategy_returns)

def get_max_drawdown(cum_series):
    """计算最大回撤。

    Args:
        cum_series (pandas.Series): 净值序列。

    Returns:
        float: 最大回撤，通常是一个小于等于 0 的值。
    """
    running_max = cum_series.cummax()
    drawdown = cum_series / running_max - 1
    return drawdown.min()

def evaluate_strategy(df):
    """对策略进行基础绩效评估。

    Args:
        df (pandas.DataFrame): 已包含净值列和策略收益列的数据表。

    Returns:
        dict: 基础绩效评估结果。
    """
    market_total_return = get_total_market_return(df)
    strategy_total_return = get_total_strategy_return(df)
    win_rate = get_strategy_win_rate(df)
    market_max_drawdown = get_max_drawdown(df["cum_return"].dropna())
    strategy_max_drawdown = get_max_drawdown(df["strategy_cum_return"].dropna())

    return {
        "market_total_return": market_total_return,
        "strategy_total_return": strategy_total_return,
        "win_rate": win_rate,
        "market_max_drawdown": market_max_drawdown,
        "strategy_max_drawdown": strategy_max_drawdown,
        "strategy_beats_market": strategy_total_return > market_total_return,
    }
    
def add_position_change_column(df):
    """增加仓位变化列。

    position_change 用来表示今天是否发生了仓位调整。
    在当前简单策略中：
        - 0 -> 1 表示开仓
        - 1 -> 0 表示平仓
        - 0 -> 0 或 1 -> 1 表示无交易

    Args:
        df (pandas.DataFrame): 已包含 position 列的数据表。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含 position_change 列。
    """
    df = df.copy()
    df["position_change"] = df["position"].diff().abs()
    return df

def add_cost_column(df, cost_rate=0.001):
    """增加交易成本列。

    当前简单模型中，成本 = 仓位变化 * cost_rate。

    Args:
        df (pandas.DataFrame): 已包含 position_change 列的数据表。
        cost_rate (float, optional): 单次仓位变化成本率，默认 0.001，即 0.1%。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含 cost 列。
    """
    df = df.copy()
    df["cost"] = df["position_change"] * cost_rate
    return df

def add_strategy_return_after_cost_column(df):
    """增加扣成本后的策略收益列。

    计算逻辑：
        strategy_return_after_cost = strategy_return - cost

    Args:
        df (pandas.DataFrame): 已包含 strategy_return 和 cost 列的数据表。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含 strategy_return_after_cost 列。
    """
    df = df.copy()
    df["strategy_return_after_cost"] = df["strategy_return"] - df["cost"]
    return df

def add_strategy_cum_return_after_cost_column(df):
    """增加扣成本后的策略累计净值列。

    Args:
        df (pandas.DataFrame): 已包含 strategy_return_after_cost 列的数据表。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含 strategy_cum_return_after_cost 列。
    """
    df = df.copy()
    df["strategy_cum_return_after_cost"] = (1 + df["strategy_return_after_cost"]).cumprod()
    return df

def build_strategy_dataframe_with_cost(df, cost_rate=0.001):
    """构建包含交易成本的完整策略研究表。

    执行步骤：
        1. 构建基础策略表
        2. 增加仓位变化列
        3. 增加成本列
        4. 增加扣成本后的策略收益列
        5. 增加扣成本后的策略累计净值列

    Args:
        df (pandas.DataFrame): 原始行情表。
        cost_rate (float, optional): 单次交易成本率，默认 0.001。

    Returns:
        pandas.DataFrame: 包含交易成本影响的完整策略表。
    """
    df = build_strategy_dataframe(df)
    df = add_position_change_column(df)
    df = add_cost_column(df, cost_rate=cost_rate)
    df = add_strategy_return_after_cost_column(df)
    df = add_strategy_cum_return_after_cost_column(df)
    return df

def add_ma_features(df, short_window, long_window):
    """增加自定义短均线和长均线列。

    Args:
        df (pandas.DataFrame): 原始行情表，必须包含 close 列。
        short_window (int): 短均线窗口。
        long_window (int): 长均线窗口。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含 return、短均线、长均线。
    """
    df = df.copy()
    df["return"] = df["close"].pct_change()
    df[f"ma_{short_window}"] = df["close"].rolling(short_window).mean()
    df[f"ma_{long_window}"] = df["close"].rolling(long_window).mean()
    return df

def add_ma_signal_column(df, short_window, long_window):
    """根据自定义短均线和长均线生成信号列。

    规则：
        - 当短均线 > 长均线时，signal = 1
        - 否则 signal = 0

    Args:
        df (pandas.DataFrame): 已包含对应均线列的数据表。
        short_window (int): 短均线窗口。
        long_window (int): 长均线窗口。

    Returns:
        pandas.DataFrame: 新的 DataFrame 副本，包含 signal 列。
    """
    df = df.copy()
    short_col = f"ma_{short_window}"
    long_col = f"ma_{long_window}"

    df["signal"] = 0
    df.loc[df[short_col] > df[long_col], "signal"] = 1
    return df

def build_ma_strategy_dataframe(df, short_window, long_window):
    """构建自定义均线参数的策略研究表。

    Args:
        df (pandas.DataFrame): 原始行情表，至少包含 close 列。
        short_window (int): 短均线窗口。
        long_window (int): 长均线窗口。

    Returns:
        pandas.DataFrame: 完整策略表。
    """
    if short_window >= long_window:
        raise ValueError("short_window 必须小于 long_window")

    df = add_ma_features(df, short_window, long_window)
    df = add_ma_signal_column(df, short_window, long_window)
    df = add_position_column(df)
    df = add_strategy_return_column(df)
    df = add_cumulative_return_columns(df)
    return df

def build_ma_strategy_dataframe_with_cost(df, short_window, long_window, cost_rate=0.001):
    """构建包含交易成本的自定义均线参数策略表。

    Args:
        df (pandas.DataFrame): 原始行情表。
        short_window (int): 短均线窗口。
        long_window (int): 长均线窗口。
        cost_rate (float, optional): 交易成本率。

    Returns:
        pandas.DataFrame: 包含交易成本影响的完整策略表。
    """
    df = build_ma_strategy_dataframe(df, short_window, long_window)
    df = add_position_change_column(df)
    df = add_cost_column(df, cost_rate=cost_rate)
    df = add_strategy_return_after_cost_column(df)
    df = add_strategy_cum_return_after_cost_column(df)
    return df

def summarize_ma_strategy(df, short_window, long_window):
    """汇总单组均线参数策略表现。

    Args:
        df (pandas.DataFrame): 原始行情表。
        short_window (int): 短均线窗口。
        long_window (int): 长均线窗口。

    Returns:
        dict: 单组参数的策略表现摘要。
    """
    strategy_df = build_ma_strategy_dataframe(df, short_window, long_window)

    market_final = strategy_df["cum_return"].dropna().iloc[-1]
    strategy_final = strategy_df["strategy_cum_return"].dropna().iloc[-1]

    return {
        "short_window": short_window,
        "long_window": long_window,
        "market_return_pct": (market_final - 1) * 100,
        "strategy_return_pct": (strategy_final - 1) * 100,
    }
    
def summarize_ma_strategy_with_cost(df, short_window, long_window, cost_rate=0.001):
    """汇总单组均线参数策略表现（含交易成本）。

    Args:
        df (pandas.DataFrame): 原始行情表。
        short_window (int): 短均线窗口。
        long_window (int): 长均线窗口。
        cost_rate (float, optional): 交易成本率。

    Returns:
        dict: 单组参数的策略表现摘要。
    """
    strategy_df = build_ma_strategy_dataframe_with_cost(
        df,
        short_window=short_window,
        long_window=long_window,
        cost_rate=cost_rate,
    )

    market_final = strategy_df["cum_return"].dropna().iloc[-1]
    strategy_final = strategy_df["strategy_cum_return"].dropna().iloc[-1]
    strategy_after_cost_final = strategy_df["strategy_cum_return_after_cost"].dropna().iloc[-1]

    return {
        "short_window": short_window,
        "long_window": long_window,
        "market_return_pct": (market_final - 1) * 100,
        "strategy_return_pct": (strategy_final - 1) * 100,
        "strategy_return_after_cost_pct": (strategy_after_cost_final - 1) * 100,
    }