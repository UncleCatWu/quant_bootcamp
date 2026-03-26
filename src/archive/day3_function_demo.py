# def say_hello():
#     print("欢迎来到 Day3")
# say_hello()

# def show_ticker(ticker):
#     print("股票代码:", ticker)
# show_ticker("AAPL")
# show_ticker("TSLA")

# def add(a,b):
#     result = a + b
#     return result

# x = add(3, 5)
# print(x)

# def show_price(price):
#     print(price)
    
# def get_total_return(first_price, last_price):
#     return (last_price / first_price) - 1

from market_utils import (
    get_total_return,
    get_average_price,
    get_highest_price,
    get_lowest_price,
)

prices = [210, 212, 208, 215, 218, 216, 220]

first_price = prices[0]
last_price = prices[-1]

total_return = get_total_return(first_price, last_price)
average_price = get_average_price(prices)
highest_price = get_highest_price(prices)
lowest_price = get_lowest_price(prices)

print("累计收益率:", round(total_return, 4))
print("累计收益率(%):", round(total_return * 100, 2))
print("平均价格:", round(average_price, 2))
print("最高价:", highest_price)
print("最低价:", lowest_price)