import numpy as np
import matplotlib.pyplot as plt
#elements must be of same type

a = np.array([0,1,2,3])

print(type(a))
print(a.dtype)
print(a.size)
print(a.shape) #tuple of ints indicating size of array in each dimension
print(a.ndim) #number of array dimensions or rank of the array

b = np.array([3.1,11.02,6.2, 213.2, 5.2])
print(b.dtype)

#slicing and indexing numpy
c = np.array([20,1,2,3,4])
c[0] = 100
print(c)
c[4] = 1
print(c)

d = c[1:4]
print(d)

c[3:5]=300, 400
print(c)

#Vector add and subtract
# u = [1 over 0] v = [0 over 1] z = u+v
#first component of z is 1+0 second is bottom 0+1 so z is [1 over 1]

# if u is [1 over 0] direction of 1 is horizontal --> and 0 is vertical in this case 0 doesn't move up or down
# v is [0 over 1] it does not point horizontal, but goes up 1 vertical
# z = u+v which is [1 over 1] match the endpoints of the tail and you get a triangle shape in graph

u = [1,0]
v = [1,0]
z=[]
# for n, m in zip(u,v):
#     z.append(n+m)
#Or one line
z = u+v
print(z)

#array multiplication with scalar
# y = [1 over 2]
# z = 2y = [2(1) over 2(2)] = [2 over 4]

y = np.array([1,2])
z=2*y
print(z)

#Product of 2 numpy arrays
# u = [1 over 2] v = [3 over 2]
#hadamard product of u and v is a new vector z
# z = u dot v = [top 1*3] [bottom 2*2]

#Dot product
# u = [1 over 2], v = [3 over 1]
# u ^t v = 1*3 + 2*1 = 5


#Add constant to numpy array
k = np.array([1,2,3,-1])
k2 = k+1
print(k2)

#Universal Function
a1 = np.array([1,-1,1,-1])
mean_a1 = a1.mean()
print(mean_a1)

max_a1 = a1.max()
print(max_a1)
np.pi
np.sin(a1)
print(np.linspace(-2,2,num=9))

# %matplotlib inline
# x= np.linspace(0,2*np.pi,100)
# y=np.sin(x)
# plt.plot(x,y)

a5 = np.array([1,-1])*np.array([1,1])
print(a5)

a6 = np.dot(np.array([1,-1]),np.array([1,1]))
print(a6)

A=np.array([[1,2],[3,4],[5,6],[7,8]])

B=np.array([[1,2,3],[4,5,6],[7,8,9]])

# ab =np.dot(A,B)
# print(ab)

#Review
# a=np.array([0,1,0,1,0])
#
# b=np.array([1,0,1,0,1])
#
# print(a*b)

# a=np.array([0,1])
#
# b=np.array([1,0])
#
# np.dot(a,b)

a=np.array([1,1,1,1,1])

print(a+10)