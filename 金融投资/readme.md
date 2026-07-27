# 金融投资

> 从零开始学**炒股**与买**基金**。每个主题分 **入门**（概念扫盲）、**进阶**（方法体系）、**术语表**（速查）、**实战案例**（方法演示）。内容结合宏观—行业—个股研究框架、估值与技术分析、定投与资产配置，并附可引用的开源量化项目。

---

## 板块导航

- [炒股](炒股/readme.md) —— 股票是什么、市场规则、基本面/技术分析、仓位管理、策略与交易心理
- [基金](基金/readme.md) —— 基金类型与运作、定投进阶、资产配置、筛选指标、组合构建

---

## 学习路径建议

```
新手 → 炒股/入门 → 基金/入门 （建立基础认知）
  ↓
进阶 → 炒股/进阶 → 基金/进阶 （搭建方法体系）
  ↓
工具 → 术语表（速查）+ 实战案例（演练）
  ↓
实践 → 模拟盘 → 小额定投/小仓实盘 → 持续复盘
```

> ⚠️ 永远顺序：先学习、再模拟、后实盘；只用闲钱，不借钱不加杠杆。

---

## 两大主题速览

| 主题 | 适合人群 | 核心方法 | 风险 | 起点建议 |
| --- | --- | --- | --- | --- |
| 炒股 | 想深入研究个股、能承受波动 | 基本面+技术面+仓位管理 | 高（个股可腰斩/退市） | 先模拟盘，买懂的公司 |
| 基金 | 没时间研究、求省心 | 宽基定投+资产配置 | 中（看类型） | 宽基指数定投起步 |

---

## 可引用的开源项目（GitHub）

做数据核验、回测、组合优化时，可参考以下真实开源项目（均已核实存在）：

1. **量化资源大全 [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant)**
   涵盖框架、数据、指标、组合优化、书籍的策展清单，量化入门导航首选。

2. **AI 量化平台 [microsoft/qlib](https://github.com/microsoft/qlib)**
   微软开源，内置因子库与机器学习模板（LightGBM/Transformer），适合因子与组合回测研究。

3. **回测框架 [backtrader/backtrader](https://github.com/backtrader/backtrader)**
   事件驱动回测，约 50 行跑一个双均线策略；配 TA-Lib 计算技术指标。

4. **国产量化框架 [vnpy/vnpy](https://github.com/vnpy/vnpy)（VeighNa）**
   支持 CTP 期货等；实盘需自担合规与风控（A股禁未许可程序化自动报单）。

5. **A股数据接口 [akfamily/akshare](https://github.com/akfamily/akshare)**
   纯 Python、无依赖，覆盖 A股/港股/期货/基金实时与历史数据；定投估值分位、资金流核验神器。

6. **A股数据 [waditu/tushare](https://github.com/waditu/tushare)（TuShare）**
   中文用户首选，A股/基金/宏观数据，Pro 版需积分。

7. **开源彭博终端 [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB)**
   统一股票/宏观数据接口，可跑 MCP 让 AI Agent 直接查金融数据。

8. **A股回测 [rqalpha/rqalpha](https://github.com/rqalpha/rqalpha)（RQAlpha）**
   米筐开源版，A股回测 API 优雅，适合教学与学术研究。

9. **组合优化 [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt)**
   马科维茨均值-方差、Black-Litterman 等资产配置算法实现。

---

## 风险与合规提醒
- 内容**仅供学习，不构成任何投资建议**。市场有风险，投资需谨慎。
- A股实行 T+1、涨跌停限制；程序化自动报单需券商/监管许可，个人多用"信号提醒+人工按键"。
- 警惕"内幕消息""稳赚战法""AI 稳赚"等宣传；回测好看不代表实盘盈利（过拟合风险）。

---

*投资有风险，内容仅供学习，不构成任何投资建议。*
