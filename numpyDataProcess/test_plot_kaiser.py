import numpy as np 
from matplotlib.pyplot import plot, show, legend 
from matplotlib.dates import datestr2num 
import sys 
# 将数据载入
closes=np.loadtxt('AAPL.csv', delimiter=',', usecols=(6,), 
	converters={1:datestr2num}, unpack=True) 
N = int(sys.argv[1])  # N = 5
# 调用blackman函数生成一个平滑窗并用它来平滑股价数据。
window = np.kaiser(42, 14) 
smoothed = np.convolve(window/window.sum(), closes, mode='same') 
# 绘制平滑后的股价图。
# 我们将省略最前面N个和最后面N个数据点。
# plot(window) 
plot(smoothed[N:-N], lw=2, label="smoothed") 
plot(closes[N:-N], label="closes") 
legend(loc='best') 
show()

