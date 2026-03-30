from market_utils import analyze_stock_from_csv, print_market_report

report = analyze_stock_from_csv(
    ticker="AAPL",
    market="US",
    file_path="data/aapl_sample.csv",
)

print_market_report(report)