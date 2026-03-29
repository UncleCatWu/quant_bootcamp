from market_utils import (
    load_dataframe_from_csv,
    build_strategy_dataframe,
    evaluate_strategy,
)

file_path = "data/aapl_sample.csv"

df = load_dataframe_from_csv(file_path)
df = build_strategy_dataframe(df)

result = evaluate_strategy(df)

print("=== Week 2 Day 2 策略绩效评估 ===")
print("市场总收益:", round(result["market_total_return"], 4))
print("市场总收益(%):", round(result["market_total_return"] * 100, 2))

print("策略总收益:", round(result["strategy_total_return"], 4))
print("策略总收益(%):", round(result["strategy_total_return"] * 100, 2))

print("策略日胜率:", round(result["win_rate"], 4))
print("策略日胜率(%):", round(result["win_rate"] * 100, 2))

print("市场最大回撤:", round(result["market_max_drawdown"], 4))
print("市场最大回撤(%):", round(result["market_max_drawdown"] * 100, 2))

print("策略最大回撤:", round(result["strategy_max_drawdown"], 4))
print("策略最大回撤(%):", round(result["strategy_max_drawdown"] * 100, 2))

print("策略是否跑赢市场:", result["strategy_beats_market"])