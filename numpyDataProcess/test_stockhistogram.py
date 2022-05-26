from matplotlib.finance import quotes_historical_yahoo 
import sys
from datetime import date 
import matplotlib.pyplot as plt 
import numpy as np 
today = date.today() 
start = (today.year - 1, today.month, today.day) 
symbol = 'DISH' 
if len(sys.argv) == 2: 
	symbol = sys.argv[1] 
quotes = quotes_historical_yahoo(symbol, start, today) 
# 上一步得到的股价数据存储在Python列表中。
quotes = np.array(quotes) 
close = quotes.T[4] 
# 指定合理数量的柱形，绘制分布直方图：
plt.hist(close, np.sqrt(len(close))) 
plt.show()