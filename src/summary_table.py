import pandas as pd
from market_utils import analyze_stock_from_csv, build_summary_row

stocks = [
    {"ticker": "AAPL", "market": "US", "file_path": "data/aapl_sample.csv"},
    {"ticker": "TSLA", "market": "US", "file_path": "data/tsla_sample.csv"},
    {"ticker": "CATL", "market": "CN", "file_path": "data/catl_sample.csv"},
]

rows = []

for stock in stocks:
    report = analyze_stock_from_csv(
        ticker=stock["ticker"],
        market=stock["market"],
        file_path=stock["file_path"],
    )
    rows.append(build_summary_row(report))

summary_df = pd.DataFrame(rows)
summary_df = summary_df.sort_values(by="return_pct", ascending=False)

print("=== 多股票汇总表（按收益率排序） ===")
print(summary_df)