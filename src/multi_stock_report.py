from market_utils import analyze_stock_from_csv, print_market_report

stocks = [
    {"ticker": "AAPL", "market": "US", "file_path": "data/aapl_sample.csv"},
    {"ticker": "TSLA", "market": "US", "file_path": "data/tsla_sample.csv"},
    {"ticker": "CATL", "market": "CN", "file_path": "data/catl_sample.csv"},
]

for stock in stocks:
    report = analyze_stock_from_csv(
        ticker=stock["ticker"],
        market=stock["market"],
        file_path=stock["file_path"],
    )
    print_market_report(report)