import numpy as np
import sys

o, h, l, c = np.loadtxt('BHP.csv', delimiter=',',
            usecols=(3, 4, 5, 6), unpack=True)
def calc_profit(open, high, low, close):
    # 在开盘时买入
    # 我们尝试以比开盘价稍低一点的价格买入股票。
    buy = open * float(sys.argv[1])
    # 如果这个价格在当日的股价范围内，
    # 我们将以当日收盘价卖出，所获得的利润即买入和卖出的差价。
    # 当日股价区间
    if low < buy < high:
        return (close - buy)/buy
    # 否则，则尝试买入失败，没有获利，也没有亏损，我们均返回0。
    else:
        return 0

# vectorize函数相当于Python中的map函数
func = np.vectorize(calc_profit)
# 对股价数组使用我们得到的func函数
profits = func(o, h, l, c)
print("Profits", profits)
# 选择非零利润的交易日并计算平均值：
real_trades = profits[profits != 0]
print("Number of trades", len(real_trades), 
    round(100.0 * len(real_ trades)/len(c),2), "%")
print("Average profit/loss %", round(np.mean(real_trades) * 100, 2))
# 乐观的人们对于正盈利的交易更感兴趣。选择正盈利的交易日并计算平均利润
winning_trades = profits[profits > 0]
print("Number of winning trades", len(winning_trades), 
    round(100.0 * len(winning_trades)/len(c), 2), "%")
print("Average profit %", round(np.mean(winning_trades) * 100, 2))
# 悲观的人们对于负盈利的交易更感兴趣，选择负盈利的交易日并计算平均损失
losing_trades = profits[profits < 0]
print("Number of losing trades", len(losing_trades), 
    round(100.0 * len(losing_trades)/len(c), 2), "%")
print("Average loss %", round(np.mean(losing_trades) * 100, 2))
