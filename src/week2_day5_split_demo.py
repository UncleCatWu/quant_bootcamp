from market_utils import load_dataframe_from_csv

file_path = "data/aapl_sample.csv"
df = load_dataframe_from_csv(file_path)

split_ratio = 0.7
split_idx = int(len(df) * split_ratio)

train_df = df.iloc[:split_idx].copy()
test_df = df.iloc[split_idx:].copy()

print("=== Week 2 Day 5 数据切分示例 ===")
print("总行数:", len(df))
print("切分位置:", split_idx)
print("训练集行数:", len(train_df))
print("测试集行数:", len(test_df))

print("\n=== 训练集 ===")
print(train_df)

print("\n=== 测试集 ===")
print(test_df)