# coding: utf-8
import numpy as np

# 我们来计算简单收益率
c=np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True) 
# diff函数可以返回一个由相邻数组元素的差值构成的数组。这有点类似于微积分中的微分。
# 因为diff返回的数组比收盘价数组少一个，c[ : -1]也忽略最后一个元素。
returns = np.diff( c ) / c[ : -1] 
# 用std函数计算标准差。
print("Standard deviation =", np.std(returns))
# 下面计算对数收益率。
# 先用log函数得到每一个收盘价的对数，再对结果使用diff函数即可。
logreturns = np.diff( np.log(c) ) 
# 根据指定的条件返回所有满足条件的数组元素的索引值。
posretindices = np.where(returns > 0) 
# 即可输出该数组中所有正值元素的索引。
print("Indices with positive returns", posretindices)
# 年波动率等于对数收益率的标准差除以其均值，再除以交易日倒数的平方根。
annual_volatility = np.std(logreturns)/np.mean(logreturns) 
annual_volatility = annual_volatility / np.sqrt(1./252.) 
print("Annual volatility", annual_volatility)
# 与计算年波动率的方法类似，计算月波动率。
print("Monthly volatility", annual_volatility * np.sqrt(1./12.))
