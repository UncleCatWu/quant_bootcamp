import pandas as pd

df = pd.read_csv("data/aapl_sample.csv")

print("原始数据:")
print(df)

#pct_change() computes the percentage change between the current and previous row.每日收益率
df["return"] = df["close"].pct_change()

print("\n加入收益率后的数据:")
print(df)

mean_return = df["return"].mean()

print("\n平均日收益率:", mean_return)
print("平均日收益率(%):", mean_return * 100)

max_close = df["close"].max()
min_close = df["close"].min()
print("\n最高收盘价:", max_close)
print("最低收盘价:", min_close)

first_close = df["close"].iloc[0]
last_close = df["close"].iloc[-1]
total_return = (last_close / first_close) - 1

print("累计收益率:", total_return)
print("累计收益率(%):", total_return * 100)

up_days = (df["return"] > 0).sum()
down_days = (df["return"] < 0).sum()

print("上涨天数:", up_days)
print("下跌天数:", down_days)

#prices = [100, 102, 101, 105, 110]

#first_price = prices[0]
#last_price = prices[-1]
#first_price = Decimal(str(prices[0]))
#last_price = Decimal(str(prices[-1]))

#total_return = (last_price / first_price) - 1

#print("初始价格:", first_price)
#print("最终价格:", last_price)
#print("总收益率:", total_return)
#print("总收益率(%):", total_return * 100)
#print("总收益率:", round(total_return, 4))
#print("总收益率(%):", round(total_return * 100, 2))
#print("总收益率(%):", "{:.2f}".format(total_return * 100))
