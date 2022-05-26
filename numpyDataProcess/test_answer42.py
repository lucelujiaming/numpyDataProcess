import numpy as np

# 定义一个Python函数
def ultimate_answer(a):
    # 使用zeros_like函数创建一个和a形状相同，
    # 并且元素全部为0的数组result
    result = np.zeros_like(a)
    # 将所有元素设置为“终极答案”其值为42
    result.flat = 42
    return result
# 使用frompyfunc创建通用函数
ufunc = np.frompyfunc(ultimate_answer, 1, 1)
print("The answer", ufunc(np.arange(4)))
# 可以对二维数组进行完全一样的操作
print("The answer", ufunc(np.arange(4).reshape(2, 2)))
