# -*- coding: utf-8 -*-
# Python Arrays etc.
from scipy import *
# import scipy as sp
import numpy as np

# // *---------------------------------------------------------------------* //

# 1D arbitrary array
x = np.array([2, 3, 1, 0])

# mixed type array
x = np.array([[1, 2.0], [0, 0], (1+1j, 3.)])

# complex array
x = np.array([[1.+0.j, 2.+0.j], [0.+0.j, 0.+0.j], [1.+1.j, 3.+0.j]])


# Numpy Array creation, initialization

# create zero-initialized matrix:
x = np.zeros((2, 3))     # rows,cols

# create zero-initialized matrix:
x = np.ones((2, 3))     # rows,cols


# using Arange:
# arange() will create arrays with regularly incrementing values.
# 1D linear array 0, 1, 2, ..., 9
np.arange(10)

# 1D linear array from 2 - 10 of type float
np.arange(2, 10, dtype=np.float)

# 1D linear array from 2 - 3 increments of 0.1
np.arange(2, 3, 0.1)

# using linspace
# The advantage of this creation function is that one can guarantee
# the number of elements and the starting and end point, which arange()
# generally will not do for arbitrary start, stop, and step values.

# create a 6 element array from 1 to 5
x = np.linspace(1., 5., 6)


# Numpy Arrays

# 2D array
x = array([(1.5, 2, 3), (4, 5, 6)])
# complex array
x = array([[1, 2], [3, 4]], dtype=complex)

x = zeros((3, 4), dtype=int16)
# confirm data type:
x.dtype

x = ones((2, 3, 4), dtype=int32)
x.dtype

# define linspace of 100 values from 0 to 2*pi:
x = linspace(0, 2*pi, 100)
f = sin(x)

# print array -> displays array in console:

# print rules:
# **the last axis is printed from left to right
# **the second-to-last is printed from top to bottom
# the rest are also printed from top to bottom, 
# with each slice separated from the next by an empty line


# 1D array
x = arange(6)
print(x)

# 2D array
# create 12 element array, reshape to 4x3
x = arange(12).reshape(4, 3)
print(x)

# 3D array
x = arange(24).reshape(2, 3, 4)
print(x)

# basic operations:
# Arithmetic operators on arrays apply elementwise:
a = array([20, 30, 40, 50])
b = arange(4)
c = a-b
# prints c = [20 29 38 47]

b**2
# prints [0 1 2 3]

# the product operator '*' operates elementwise in NumPy arrays
# The matrix product can be performed using the dot function
# or by creating matrix objects

A = array( [[1, 1], [0, 1]] )
B = array( [[2, 0], [3, 4]] )
A*B
# print [[2,0], [0,4]]
dot(A, B)
# print [[5,4], [3,4]]

# Some operations, such as += and *=, act in place to modify an existing array
a = ones((2, 3), dtype=int)
# >>> print a
# [[1 1 1]
#  [1 1 1]]
b = random.random((2, 3))
# >>> print b
# [[ 0.49937158  0.80214821  0.51157973]
#  [ 0.25961988  0.25100275  0.99972712]]

# numpy random number generator (floats!)
c = np.random.random_sample((5,))
# >>> c
# array([ 0.92532941,  0.40888658,  0.84251106,  0.77973772,  0.97121246])

# to define a range for random number vectors
# for half-closed interval [a,b) => mpy by b-a, then add a
# example, for 8-t, range = -128 <-> 127:
a = -2**7
b = 2**7-1
d = (b - a)*np.random.random_sample((10000,)) + a
# d = ((2**7 - 1) - (-2**7))*np.random.random_sample((10000,)) + (-2**7)


a *= 3
# print a
# [[3 3 3]
#  [3 3 3]]

b += a
# >>> print b
# [[ 3.49937158  3.80214821  3.51157973]
#  [ 3.25961988  3.25100275  3.99972712]]

a += b    # b is converted to integer type
# >>> print a
# [[6 6 6]
#  [6 6 6]]


# *methods of the ndarray class*
# Many unary operations, such as computing the sum of all
# the elements in the array, are implemented as methods of the ndarray class.

a = random.random((2, 3))
a.sum()
# outputs sum of all elements
a.min()
# outputs min element value
a.max()
# outputs max element value

# By default, these operations apply to the array as though it were a list
# of numbers, regardless of its shape. However, by specifying the axis
# parameter you can apply an operation along the specified axis of an array:

b = arange(12).reshape(3, 4)
# >>> print b
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

b.sum(axis=0)    # sum of each column
# array([12, 15, 18, 21])

b.min(axis=1)   # min of each row
# array([0, 4, 8])

b.cumsum(axis=1)    # cumulative sum along each row
# array([[ 0,  1,  3,  6],
#        [ 4,  9, 15, 22],
#        [ 8, 17, 27, 38]])


# Universal Functions
# NumPy provides familiar mathematical functions such as sin, cos, and exp.
# In NumPy, these are called "universal functions"(ufunc). Within NumPy,
# these functions operate elementwise on an array, producing an array as output

B = arange(3)
# >>> print B
# [0 1 2]

exp(B)
# array([ 1.        ,  2.71828183,  7.3890561 ])

sqrt(B)
# array([ 0.        ,  1.        ,  1.41421356])

C = array([2., -1., 4.])

add(B, C)
# array([ 2.,  0.,  6.])


# **Indexing, Slicing and Iterating**
# One-dimensional arrays can be indexed, sliced and iterated over, much like
# lists and other Python sequences

a = arange(10)**3
# >>> print a
# [  0   1   8  27  64 125 216 343 512 729]

a[2]
# 8

a[2:5]
# array([ 8, 27, 64])

# equivalent to a[0:6:2] = -1000:
# from start to position 6, exclusive, set every 2nd element to -1000
a[:6:2] = -1000
# >>> print a
# [-1000     1 -1000    27 -1000   125   216   343   512   729]

# OR
a = arange(10)**3
a[:len(a):2] = 777
# >>> print a
# [777   1 777  27 777 125 777 343 777 729]

# **Reverse array**:
a[::-1]
# array([729, 777, 343, 777, 125, 777,  27, 777,   1, 777])

d = arange(11)
# >>> d
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
d[::-1]
# array([10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0])


# **periodic slice of array**:
d = arange(11)
d[::2]
# array([ 0,  2,  4,  6,  8, 10])

d = arange(11)
d[::-2]
# array([10,  8,  6,  4,  2,  0])

d = arange(11)
d[::-3]
# array([10,  7,  4,  1])


# **Multi-Dimentional Arrays**
# Multidimensional arrays can have one index per axis. These indices are
# given in a tuple separated by commas:

def f(x, y):
    return 10*x+y

b = fromfunction(f, (5, 4), dtype=int)
# >>> b
# array([[ 0,  1,  2,  3],
#        [10, 11, 12, 13],
#        [20, 21, 22, 23],
#        [30, 31, 32, 33],
#        [40, 41, 42, 43]])

# single array element index
b[2, 3]
# 23

# slice out 2nd column:
b[0:5, 1]
# array([ 1, 11, 21, 31, 41])

# same as above!!
b[ : ,1]
# array([ 1, 11, 21, 31, 41]

# slice out each column in the second and third row of b
# ** [1:3 ... from position '2' until but not including '4'
# i.e. rows 2 & 3
b[1:3, :]
# array([[10, 11, 12, 13],
#        [20, 21, 22, 23]])

# **When fewer indices are provided than the number of axes, the missing
# indices are considered complete slices:

# slice out the first row of the array:
b[0]
# array([0, 1, 2, 3])

# slice out the third row of the array:
b[2]
array([20, 21, 22, 23])

# slice out the last row of the array:
b[-1]
# OR
b[-1, :]
# array([40, 41, 42, 43])

# slice out the second to last row of the array:
b[-2]
# array([30, 31, 32, 33])


# **Iterating over a multi-dimentional array
# Iterating over multidimensional arrays is done with respect to the first axis
for row in b:
    print(row)
# [0 1 2 3]
# [10 11 12 13]
# [20 21 22 23]
# [30 31 32 33]
# [40 41 42 43]

# in order to iterate over each array element, use the 'flat' attribute
for element in b.flat:
    print(element)
# 0 1 2 3 10 11 12 13 20 21 22 23 30 31 32 33 40 41 42 43
# **note, print element, -> prints elements as a row
# **note, print element  -> prints elements as a column
# only affects console display printing..


# **Shape Manipulation**
# An array has a shape given by the number of elements along each axis:
a = floor(10*random.random((3, 4)))
# >>> a
# array([[ 8.,  2.,  8.,  1.],
#        [ 0.,  9.,  6.,  3.],
#        [ 1.,  4.,  2.,  4.]])

a.shape
# (3, 4)

# flatten the array:
a.ravel()
# array([ 8.,  2.,  8.,  1.,  0.,  9.,  6.,  3.,  1.,  4.,  2.,  4.])

# Force the shape to specific dimension
a.shape = (6, 2)
# >>> a
# array([[ 8.,  2.],
#        [ 8.,  1.],
#        [ 0.,  9.],
#        [ 6.,  3.],
#        [ 1.,  4.],
#        [ 2.,  4.]])

# transpose array:
a.transpose()
# array([[ 8.,  8.,  0.,  6.,  1.,  2.],
#        [ 2.,  1.,  9.,  3.,  4.,  4.]])

# transpose array alt:
aa = floor(10*random.random((2, 7)))

aa.T
# array([[ 5.,  1.],
#        [ 1.,  3.],
#        [ 2.,  9.],
#        [ 1.,  0.],
#        [ 1.,  4.],
#        [ 7.,  6.],
#        [ 7.,  9.]])


# 3D 'list'    (**useless**)
zlist = [[[1,2,3],[21,22,23],[31,32,33]],[[41,42,43],[51,52,53],[61,62,63]],[[71,72,73],[81,82,83],[91,92,93]]]

# 3D array    (**useful**)
z = np.array([[[1,2,3],[21,22,23],[31,32,33]],[[41,42,43],[51,52,53],[61,62,63]],[[71,72,73],[81,82,83],[91,92,93]]])

  
# zip
x = [1, 2, 3]
y = [4, 5, 6]
myZip = zip(x, y)
# >>> myZip
# [(1, 4), (2, 5), (3, 6)]
x2, y2 = zip(*myZip)
x == list(x2) and y == list(y2)
# True

# // *---------------------------------------------------------------------* //

# http://docs.scipy.org/doc/numpy-1.5.x/reference/arrays.indexing.html

# Basic Slicing - syntax is [i:j:k]
# i = starting index; j = stopping index; k = the step (k !=0)

# Negative i and j
# a negative k makes stepping go towards smaller indices

# Define ex array
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# slicing from 1 until 7, start at 1, output every 2nd element
x[1:7:2]
# >>>array([1, 3, 5])

x[5:]
# >>>array([5, 6, 7, 8, 9])

x[5:9]
# >>>array([5, 6, 7, 8])

x[9:5:-1]
# >>>array([9, 8, 7, 6])


# :::2D slicing examples:::

x2d = np.ones([6, 6])
# >>> x2d
# array([[ 1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.]])

x2d[0:3, 0:3] = np.ones([3, 3])*5
# >>> x2d
# array([[ 5.,  5.,  5.,  1.,  1.,  1.],
#        [ 5.,  5.,  5.,  1.,  1.,  1.],
#        [ 5.,  5.,  5.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.]])

x2d[3:6, 3:6] = np.ones([3, 3])*6
# >>> x2d
# array([[ 5.,  5.,  5.,  1.,  1.,  1.],
#        [ 5.,  5.,  5.,  1.,  1.,  1.],
#        [ 5.,  5.,  5.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  6.,  6.,  6.],
#        [ 1.,  1.,  1.,  6.,  6.,  6.],
#        [ 1.,  1.,  1.,  6.,  6.,  6.]])

x2dSub1 = x2d[0:3, 0:3]
# >>> x2dSub1
# array([[ 5.,  5.,  5.],
#        [ 5.,  5.,  5.],
#        [ 5.,  5.,  5.]])

x2dSub2 = x2d[1:5, 1:5]
# >>> x2dSub2
# array([[ 5.,  5.,  1.,  1.],
#        [ 5.,  5.,  1.,  1.],
#        [ 1.,  1.,  6.,  6.],
#        [ 1.,  1.,  6.,  6.]])


# Define 1D monotonic array, reshape and transpose:
x2Drs = np.arange(36).reshape(6, 6).T
# >>> x2Drs
# array([[ 0,  6, 12, 18, 24, 30],
#        [ 1,  7, 13, 19, 25, 31],
#        [ 2,  8, 14, 20, 26, 32],
#        [ 3,  9, 15, 21, 27, 33],
#        [ 4, 10, 16, 22, 28, 34],
#        [ 5, 11, 17, 23, 29, 35]])


# 2D Slicing with stride(?)

# outputs every 2nd
x2DrsSub1 = x2Drs[1:6:2, 1:6:2]
# >>> x2DrsSub1
# array([[ 7, 19, 31],
#        [ 9, 21, 33],
#        [11, 23, 35]])

# outputs every 3rd
x2DrsSub2 = x2Drs[0:6:3, 0:6:3]
# >>> x2DrsSub2
# array([[ 0, 18],
#        [ 3, 21]])






# // *---------------------------------------------------------------------* //


# <<concatenating mx(arbitrary-n) 2D data with key>>
# **variable column length

# define dimensions:
row = 3
col1 = 6
col2 = 7
col3 = 5
col4 = 11
time1 = 555
time2 = 666
time3 = 777
time4 = 888
# create several dummy arrays:
aC2D = np.zeros((row, col1))
bC2D = np.ones((row, col2))
cC2D = arange(row*col3).reshape(row, col3)
dC2D = floor(10*random.random((row, col4)))

# initialize MatchBuff with first 2D array
MatchBuff = aC2D
indexKey = [1]
lengthKey = [col1]
timeKey = [time1]
offsetKey = [0.0]
MatchBuffKey = np.array([indexKey, lengthKey, timeKey, offsetKey])
MatchBuffKey = MatchBuffKey.transpose()

print('\n')
print(MatchBuffKey)

# create a 'key' signal
aC2DKey = np.append([1, len(aC2D[1, :]), time1, MatchBuffKey[0, 3]], np.zeros((1, len(aC2D[1, :])-4)))
# combine key signal with current 2D array
# aC2DComb = np.append(aC2DKey,aC2D.flatten()).reshape(row+1,len(aC2DKey))
MatchBuff = np.append(aC2DKey, aC2D.flatten()).reshape(row+1, len(aC2DKey))

# concatenate each new 2D array + key
# iteration 1:
indexKey = np.append(indexKey, 2)
lengthKey = np.append(lengthKey, col2)
timeKey = np.append(timeKey, time2)
# calculate current total offset
offsetKey = np.append(offsetKey, lengthKey[:len(lengthKey)-1].sum())
MatchBuffKey = np.array([indexKey, lengthKey, timeKey, offsetKey])
MatchBuffKey = MatchBuffKey.transpose()

print('\n')
print(MatchBuffKey)


bC2DKey = np.append([2, len(bC2D[1, :]), time2, MatchBuffKey[1, 3]], np.zeros((1, len(bC2D[1, :])-4)))
bC2DComb = np.append(bC2DKey, bC2D.flatten()).reshape(row+1, len(bC2DKey))

MatchBuff = concatenate((MatchBuff, bC2DComb), 1)

# iteration 2:
indexKey = np.append(indexKey, 3)
lengthKey = np.append(lengthKey, col3)
timeKey = np.append(timeKey, time3)
# calculate current total offset
offsetKey = np.append(offsetKey, lengthKey[:len(lengthKey)-1].sum())
MatchBuffKey = np.array([indexKey, lengthKey, timeKey, offsetKey])
MatchBuffKey = MatchBuffKey.transpose()

print('\n')
print(MatchBuffKey)


cC2DKey = np.append([3, len(cC2D[1, :]), time3, MatchBuffKey[2, 3]], np.zeros((1, len(cC2D[1, :])-4)))
cC2DComb = np.append(cC2DKey, cC2D.flatten()).reshape(row+1, len(cC2DKey))

MatchBuff = concatenate((MatchBuff, cC2DComb), 1)

# iteration 3:
indexKey = np.append(indexKey, 4)
lengthKey = np.append(lengthKey, col4)
timeKey = np.append(timeKey, time4)
# calculate current total offset
offsetKey = np.append(offsetKey, lengthKey[:len(lengthKey)-1].sum())
MatchBuffKey = np.array([indexKey, lengthKey, timeKey, offsetKey])
MatchBuffKey = MatchBuffKey.transpose()

print('\n')
print(MatchBuffKey)


dC2DKey = np.append([4, len(dC2D[1, :]), time4, MatchBuffKey[3, 3]], np.zeros((1, len(dC2D[1, :])-4)))
dC2DComb = np.append(dC2DKey, dC2D.flatten()).reshape(row+1, len(dC2DKey))

MatchBuff = concatenate((MatchBuff, dC2DComb), 1)

print('\n')
print(MatchBuff)

# print individual 2D arrays:
print('\n')
print('MatchBuff first Block')
BlockIndex = 1
print(MatchBuff[:, MatchBuffKey[BlockIndex-1, 3]:MatchBuffKey[BlockIndex-1, 3]+MatchBuffKey[BlockIndex-1, 1]])

print('\n')
print('MatchBuff Second Block')
BlockIndex = 2
print(MatchBuff[:, MatchBuffKey[BlockIndex-1, 3]:MatchBuffKey[BlockIndex-1, 3]+MatchBuffKey[BlockIndex-1, 1]])

print('\n')
print('MatchBuff Third Block')
BlockIndex = 3
print(MatchBuff[:, MatchBuffKey[BlockIndex-1, 3]:MatchBuffKey[BlockIndex-1, 3]+MatchBuffKey[BlockIndex-1, 1]])

print('\n')
print('MatchBuff Fourth Block')
BlockIndex = 4
print(MatchBuff[:, MatchBuffKey[BlockIndex-1, 3]:MatchBuffKey[BlockIndex-1, 3]+MatchBuffKey[BlockIndex-1, 1]])


# <<appending mxn 2D arrays into 3D array>>

# define dimensions:
row = 3
col = 4

# create several dummy arrays:
a12D = np.zeros((row, col))
b12D = np.ones((row, col))
c12D = arange(row*col).reshape(row, col)
d12D = floor(10*random.random((row, col)))
# //////////////////////////////////////////////////////////////////////////////

# initialize eN2D to the first 2D array
eN2D = a12D
# consecutively append next 2D array:
# append does not preserve the correct format, so we must reshape
eN2D = np.append(eN2D, b12D).reshape(((len(eN2D.flatten())+(row*col))/(row*col), row, col))
eN2D = np.append(eN2D, c12D).reshape(((len(eN2D.flatten())+(row*col))/(row*col), row, col))
eN2D = np.append(eN2D, d12D).reshape(((len(eN2D.flatten())+(row*col))/(row*col), row, col))
