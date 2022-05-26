from matplotlib.dates import DateFormatter 
from matplotlib.dates import DayLocator 
from matplotlib.dates import MonthLocator 
# from matplotlib.finance import quotes_historical_yahoo   
# from matplotlib.finance import quotes_yahoo_historical_ohlc 
import sys 
from datetime import date 
import matplotlib.pyplot as plt 
import pandas_datareader as pdr

# 将当前的日期减去1年作为起始日期。
today = date.today() 
start = (today.year - 1, today.month, today.day) 
# 创建所谓的定位器，在x轴上定位月份和日期。
alldays = DayLocator() 
months = MonthLocator() 
# 创建一个日期格式化器以格式化x轴上的日期。
month_formatter = DateFormatter("%b %Y") 
symbol = 'DISH' 
if len(sys.argv) == 2: 
    symbol = sys.argv[1] 
# 从雅虎财经频道下载股价数据。
quotes = pdr.get_data_yahoo('INTC', '2019/10/1', '2019/11/1')
# quotes = quotes_historical_yahoo_ochl(symbol, start, today)
# 创建一个Matplotlib的figure对象——这是绘图组件的顶层容器。
fig = plt.figure() 
# 增加一个子图。
ax = fig.add_subplot(111) 
# 将x轴上的主定位器设置为月定位器。该定位器负责x轴上较粗的刻度。
ax.xaxis.set_major_locator(months) 
# 将x轴上的次定位器设置为日定位器。该定位器负责x轴上较细的刻度。
ax.xaxis.set_minor_locator(alldays) 
# 将x轴上的主格式化器设置为月格式化器。该格式化器负责x轴上较粗刻度的标签。
ax.xaxis.set_major_formatter(month_formatter) 
# 绘制K线图。
candlestick(ax, quotes) 
# 将x轴上的标签格式化为日期。为了更好地适应x轴的长度，标签将被旋转。
fig.autofmt_xdate() 
plt.show()
