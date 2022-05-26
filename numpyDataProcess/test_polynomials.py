import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

# 使用BHP和VALE的股票价格数据。
bhp=np.loadtxt("BHP.csv", delimiter=",", usecols=(6,), unpack=True)
vale=np.loadtxt("VALE.csv", delimiter=",", usecols=(6,), unpack=True)
t = np.arange(len(bhp))

# 用多项式去拟合两只股票收盘价的差价：
poly = np.polyfit(t, bhp - vale, int(sys.argv[1]))
print("Polynomial fit", poly)
# 用我们刚刚得到的多项式对象以及polyval函数，就可以推断下一个值：
print("Next value", np.polyval(poly, t[-1] + 1))
# 使用roots函数找出我们拟合的多项式函数什么时候到达0值
print("Roots", np.roots(poly))
# 使用polyder函数对多项式函数求导：
der = np.polyder(poly)
# 求出导数函数的根，即找出原多项式函数的极值点。
print("Derivative", der)
print("Extremas", np.roots(der))
# 使用polyval计算多项式函数的值：
vals = np.polyval(poly, t)
# 使用argmax和argmin找出最大值点和最小值点。
print(np.argmax(vals))
print(np.argmin(vals))
# 绘制源数据和拟合函数
plot(t, bhp - vale)
plot(t, vals)
show()
