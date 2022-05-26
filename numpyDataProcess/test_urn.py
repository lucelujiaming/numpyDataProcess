import numpy as np 
from matplotlib.pyplot import plot, show 
points = np.zeros(100) 
# 使用hypergeometric函数初始化游戏的结果矩阵。
outcomes = np.random.hypergeometric(25, 1, 3, size=len(points)) 
# 使用hypergeometric函数初始化游戏的结果矩阵。
for i in range(len(points)): 
    if outcomes[i] == 3: 
        points[i] = points[i - 1] + 1 
    elif outcomes[i] == 2: 
        points[i] = points[i - 1] - 6 
    else: 
        print("outcomes[", i ,"] : ", outcomes[i])
# 使用Matplotlib绘制points数组。
plot(np.arange(len(points)), points) 
show()