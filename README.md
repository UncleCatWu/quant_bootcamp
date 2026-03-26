

# Quant Bootcamp

一个用于学习 Python 与量化交易基础的训练项目。

## 项目目标

这个项目用于逐步搭建一个迷你量化研究框架，当前重点包括：

- 使用 Python 进行基础数据分析
- 从 CSV 文件读取股票价格数据
- 计算收益率、最高价、最低价、平均价格
- 统计上涨、下跌、平盘天数
- 使用 pandas 构建基础特征列
- 计算短期均线（MA3、MA5）
- 生成单只股票报告
- 批量分析多只股票
- 生成多股票汇总表

## 当前项目结构

```text
quant_bootcamp/
├── data/
│   ├── aapl_sample.csv
│   ├── tsla_sample.csv
│   └── catl_sample.csv
├── src/
│   ├── market_utils.py
│   ├── single_stock_report.py
│   ├── multi_stock_report.py
│   ├── summary_table.py
│   └── archive/
│       ├── day2_variables.py
│       ├── day2_list_demo.py
│       ├── day2_if_demo.py
│       ├── day3_function_demo.py
│       ├── day4_read_csv_demo.py
│       └── day5_pandas_basics.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 环境安装

先创建并激活虚拟环境：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 依赖安装

安装项目依赖：

```bash
pip install -r requirements.txt
```

## requirements.txt 内容

```text
pandas
numpy
matplotlib
```

## 运行方式

### 1. 分析单只股票

```bash
python src/single_stock_report.py
```

### 2. 批量分析多只股票

```bash
python src/multi_stock_report.py
```

### 3. 生成多股票汇总表

```bash
python src/summary_table.py
```

## 当前已实现功能

### 数据读取

- 从 CSV 文件读取股票价格数据
- 提取 `close` 列用于价格分析
- 支持将 CSV 加载为 DataFrame 或价格列表

### 基础统计分析

- 累计收益率
- 平均价格
- 最高价 / 最低价
- 上涨 / 下跌 / 平盘天数
- 价格区间
- 趋势标签
- 波动标签

### 基础特征工程

- 日收益率 `return`
- 3 日均线 `ma_3`
- 5 日均线 `ma_5`

### 简单信号生成

- 当 `ma_3 > ma_5` 时，标记为“短期偏强”
- 当 `ma_3 < ma_5` 时，标记为“短期偏弱”
- 当均线数据不足时，标记为“均线数据不足”

### 报告生成

- 单只股票详细报告
- 多只股票批量报告
- 多股票汇总表
- 汇总表支持按收益率排序

## 核心模块说明

### `src/market_utils.py`

项目核心工具模块，当前包含：

- CSV 数据读取函数
- 收益率与均线特征生成函数
- 价格统计分析函数
- 最新均线信号判断函数
- 单股分析函数
- 汇总行构建函数
- 报告打印函数

### `src/single_stock_report.py`

单只股票分析入口脚本。  
适合用于查看某一个标的的详细统计结果与最新均线信号。

### `src/multi_stock_report.py`

多只股票批量分析入口脚本。  
适合用于顺序输出多只股票的完整报告。

### `src/summary_table.py`

多股票汇总表入口脚本。  
适合用于横向比较不同标的的收益率、涨跌天数、趋势和信号。

## 示例输出

### 单只股票报告示例

```text
==============================
股票代码: AAPL
市场: US
文件路径: data/aapl_sample.csv

统计结果:
上涨天数: 6
下跌天数: 3
平盘天数: 0
累计收益率: 0.0714
累计收益率(%): 7.14
最高价: 225
最低价: 208
平均价格: 216.5
趋势判断: 这段时间整体上涨
波动判断: 波动较大

最新观察:
最新收盘价: 225
最新 3 日均线: 222.0
最新 5 日均线: 220.0
均线信号: 短期偏强
```

### 多股票汇总表示例

```text
=== 多股票汇总表（按收益率排序） ===
  ticker market  latest_close  return_pct  up_days  down_days      trend   signal
0   AAPL     US         225.0        7.14        6          3  这段时间整体上涨  短期偏强
1   CATL     CN         272.0        4.62        4          2  这段时间整体上涨  短期偏强
2   TSLA     US         310.0       -6.06        1          5  这段时间整体下跌  短期偏弱
```

## 学习重点

这个项目当前阶段重点训练以下能力：

- Python 基础语法
- 函数与模块化思维
- pandas 基础数据处理
- 从原始价格数据中构造特征
- 把分析逻辑封装成可复用工具
- 把单次脚本练习升级为小型项目结构

## 后续计划

后续会继续扩展以下内容：

- 更系统的 pandas 操作
- 更多技术指标
- 信号列生成
- 持仓列生成
- 简单策略逻辑
- 回测雏形
- 策略评估模块
- 风险控制模块
- 可视化图表
- 参数化配置
- 更规范的 Python 工程结构

## 项目定位说明

这是一个学习型项目，当前重点是训练：

- Python 编程能力
- 数据分析能力
- 量化研究思维
- 工程化代码组织能力

当前版本不用于实盘交易，也不构成任何投资建议。

## Git 使用建议

每完成一个阶段，建议使用以下命令提交代码：

```bash
git add .
git commit -m "your commit message"
git push
```

## 作者说明

这是一个持续迭代中的量化学习项目。后续会继续在此基础上扩展策略研究、回测和风险控制能力。