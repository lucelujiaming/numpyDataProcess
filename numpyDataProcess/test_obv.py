import numpy as np

# 把BHP数据分别加载到收盘价和成交量的数组中
c, v=np.loadtxt('BHP.csv', delimiter=',', usecols=(6, 7), unpack=True)
# 先使用diff函数计算收盘价的变化量
change = np.diff(c)
print("Change", change)
# sign函数可以返回数组中每个元素的正负符号
signs = np.sign(change)
print("Signs", signs)
# 用piecewise函数来获取数组元素的正负。
pieces = np.piecewise(change, [change < 0, change > 0], [-1, 1])
print("Pieces", pieces)
# 检查两次的输出是否一致
print("Arrays equal?", np.array_equal(signs, pieces))
# 计算OBV值
print("On balance volume", v[1:] * signs)


