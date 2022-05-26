import numpy as np
a = np.array([2, 6, 5])
b = np.array([1, 2, 3])
# divide函数在整数和浮点数除法中均只保留整数部分
print("Divide", np.divide(a, b), np.divide(b, a))
# 返回除法的浮点数结果
print("True Divide", np.true_divide(a, b), np.true_divide(b, a))
# floor_divide函数总是返回整数结果
print("Floor Divide", np.floor_divide(a, b), np.floor_divide(b, a))
c = 3.14 * b
print("Floor Divide 2", np.floor_divide(c, b), np.floor_divide(b, c))
# 使用/运算符相当于调用divide函数
print("/ operator", a/b, b/a)
# 运算符//对应于floor_divide函数
print("// operator", a//b, b//a)
print("// operator 2", c//b, b//c)

