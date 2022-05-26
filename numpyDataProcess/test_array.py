# coding: utf-8
from numpy import * 

a = arange(5) 
print(a.dtype)

print(a)
print(a.shape)

m = array([arange(2), arange(2)])
print(m)
print(m.shape)

a = array([[1,2],[3,4]])
print(a)
print(a[0,0])
print(a[0,1])
print(a[1,0])
print(a[1,1])

print("float64(42) :", float64(42))
print("int8(42.0) :", int8(42.0))
print("bool(42) :", bool(42))
print("bool(0) :", bool(0))
print("bool(42.0) :", bool(42.0))
print("float(True) :", float(True))
print("float(False) :", float(False))

print("arange(7, dtype=uint16) : ", arange(7, dtype=uint16))

t = dtype([('name', str_, 40), ('numitems', int32), ('price',float32)])
print("t : ", t)
print("t['name'] : ", t['name'])

itemz = array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)
print("itemz : ", itemz)
print("itemz[1] : ", itemz[1])

b = arange(24).reshape(2,3,4)
print("b : ", b)
print("b[:,0,0] : ", b[:,0,0])
print("b[0, ...] : ", b[0, ...])
print("b[0,1] : ", b[0,1])
print("b[0,1,::2] : ", b[0,1,::2])
print("b[...,1] : ", b[...,1])
print("b[:,1] : ",   b[:,1])
print("b[0,:,1] : ", b[0,:,1])
print("b[0,::2,-1] : ", b[0,::2,-1])
print("b[::-1] : ", b[::-1])

# 我们可以用ravel函数完成展平的操作
print("b.ravel() : ", b.ravel())
# flatten就是展平的意思
print("b.flatten() : ", b.flatten())
# 转置矩阵是很常见的操作
print("b.transpose() : ", b.transpose())
# 但resize会直接修改所操作的数组
print("b.resize((2,12) : ", b.resize((2,12)))

a = arange(9).reshape(3,3)
print("a : ", a)
b = 2 * a
print("b : ", b)
# 水平组合
print("hstack((a, b)) : ", hstack((a, b)))
print("concatenate((a, b), axis=1) : ", concatenate((a, b), axis=1))
# 垂直组合
print("vstack((a, b)) : ", vstack((a, b)))
print("concatenate((a, b), axis = 0) : ", concatenate((a, b), axis = 0))

print("dstack((a, b)) : ", dstack((a, b)))

oned = arange(2)
print("oned : ", oned)
twice_oned = 2 * oned
print("twice_oned : ", twice_oned)
# 列组合column_stack函数对于一维数组将按列方向进行组合
print("column_stack((oned, twice_oned)) : ", 
	column_stack((oned, twice_oned)))
print("column_stack((a, b)) : ", column_stack((a, b)))
print("column_stack((a, b)) == hstack((a, b)) : ", 
	column_stack((a, b)) == hstack((a, b)))
print("row_stack((oned, twice_oned)) : ", 
	row_stack((oned, twice_oned)))
# NumPy中也有按行方向进行组合的函数，它就是row_stack。
print("row_stack((a, b)) : ", row_stack((a, b)))
print("row_stack((a, b)) == vstack((a, b)) : ", 
	row_stack((a, b)) == vstack((a, b)))

# a = arange(9).reshape(3,3)
# 下面的代码将把数组沿着水平方向分割为3个相同大小的子数组：
print("hsplit(a, 3) : ", hsplit(a, 3))
print("split(a, 3, axis=1) : ", split(a, 3, axis=1))
# vsplit函数将把数组沿着垂直方向分割
print("vsplit(a, 3) : ", vsplit(a, 3))
print("split(a, 3, axis=0) : ", split(a, 3, axis=0))

c = arange(27).reshape(3, 3, 3)
print("c : ", c)
# dsplit函数将按深度方向分割数组
print("dsplit(c, 3) : ", dsplit(c, 3))

print("b  : ", b)
# ndim属性，给出数组的维数，或数组轴的个数
print("b.ndim : ", b.ndim)
# size属性，给出数组元素的总个数
print("b.size : ", b.size)
# itemsize属性，给出数组中的元素在内存中所占的字节数
print("b.itemsize : ", b.itemsize)
# 整个数组所占的存储空间，可以用nbytes属性来查看
print("b.nbytes : ", b.nbytes)
# T属性的效果和transpose函数一样
print("b.T : ", b.T)

# 我们可以创建一个由复数构成的数组
b = array([1.j + 1, 2.j + 3])
print("b  : ", b)
# real属性，给出复数数组的实部
print("b.real : ", b.real)
# imag属性，给出复数数组的虚部
print("b.imag : ", b.imag)
# 如果数组中包含复数元素，则其数据类型自动变为复数型
print("b.dtype : ", b.dtype)

b = arange(4).reshape(2,2)
print("b  : ", b)
# flat属性将返回一个numpy.flatiter对象
print("b.flat : ", b.flat)
# 可以用flatiter对象直接获取一个或多个数组元素
print("b.flat[[1,3]] : ", b.flat[[1,3]])
b.flat = 7
print("b  : ", b)
b.flat[[1,3]] = 1
print("b  : ", b)

b = array([1.j + 1, 2.j + 3])
print("b  : ", b)
# 转换成列表
print("b.tolist() : ", b.tolist())
bList = b.tolist()
print("b  : ", b)
# astype函数可以在转换数组时指定数据类型
print("b.astype('complex') : ", b.astype('complex'))




