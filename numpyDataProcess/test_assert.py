import numpy as np
import sys
# 来检查它们是否近似相等。
print("Decimal 6", np.testing.assert_almost_equal(0.123456789, 0.123456780,
decimal=7))
print("Decimal 7", np.testing.assert_almost_equal(0.123456789, 0.123456780,
decimal=8))
# 两个数字的近似程度是否达到指定的有效数字要求
print("Significance 8", np.testing.assert_approx_equal(0.123456789,
0.123456780,significant=8))
print("Significance 9", np.testing.assert_approx_equal(0.123456789, 0.123456780,
significant=9))
# 两个数组中元素的近似程度是否达到指定的精度要求
print("Decimal 8", np.testing.assert_array_almost_equal([0, 0.123456789], [0,
0.123456780], decimal=8))
print("Decimal 9", np.testing.assert_array_almost_equal([0, 0.123456789], [0,
0.123456780], decimal=9))
# 两个数组对象是否相同
print("Pass", np.testing.assert_allclose([0, 0.123456789, np.nan], [0, 0.123456780,
np.nan], rtol=1e-7, atol=0))
print("Fail", np.testing.assert_array_equal([0, 0.123456789, np.nan], [0, 0.123456780,
np.nan]))
# 两个数组必须形状一致并且第一个数组的元素严格小于第二个数组的元素
print("Pass", np.testing.assert_array_less([0, 0.123456789, np.nan], [1, 0.23456780,
np.nan]))
print("Fail", np.testing.assert_array_less([0, 0.123456789, np.nan], [0, 0.123456780,
np.nan]))
# 如果两个对象是否相同
print("Equal?", np.testing.assert_equal((1, 2), (1, 3)))
# 断言两个字符串变量完全相同
print "Pass", np.testing.assert_string_equal("NumPy", "NumPy")
print "Fail", np.testing.assert_string_equal("NumPy", "Numpy")
# 比较两个近似相等的浮点数
eps = np.finfo(float).eps 
print "EPS", eps
print "1", 
np.testing.assert_array_almost_equal_nulp(1.0, 1.0 + eps) 
print "2", 
np.testing.assert_array_almost_equal_nulp(1.0, 1.0 + 2 * eps)
# 指定ULP的数量作为允许的误差上界。
eps = np.finfo(float).eps 
print "EPS", eps
print "1", np.testing.assert_array_max_ulp(1.0, 1.0 + eps) 
print "2", np.testing.assert_array_max_ulp(1.0, 1 + 2 * eps, maxulp=2)












