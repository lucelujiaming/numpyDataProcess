import numpy as np 
from matplotlib.pyplot import plot, show 
# 初始化一个全0的数组来存放剩余资本。
cash = np.zeros(10000) 
cash[0] = 1000 
# 以参数10000调用binomial函数。
outcome = np.random.binomial(9, 0.5, size=len(cash)) 
#模拟每一轮抛硬币的结果并更新cash数组。
for i in range(1, len(cash)): 
    # 打印出outcome的最小值和最大值，以检查输出中是否有任何异常值
    if outcome[i] < 5: 
        cash[i] = cash[i - 1] - 1 
    elif outcome[i] < 10: 
        cash[i] = cash[i - 1] + 1 
    else: 
        raise AssertionError("Unexpected outcome " + outcome) 
print(outcome.min(), outcome.max())
# 使用Matplotlib绘制cash数组
plot(np.arange(len(cash)), cash) 
show()