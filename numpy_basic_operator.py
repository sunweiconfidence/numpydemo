import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)

print(a,b)
c = a+b
print(c)

#b的平方 
d = b ** 2
print(d)

e = 10 * np.sin(a)
print(e)

print(b)
print(b<3)

aa = np.array([[1,1],
               [0,1]])
bb = np.arange(4).reshape(2,2)
c = aa * bb
c_dot = np.dot(aa,bb)
# another write method
c_dot_2 = aa.dot(bb)
print(aa)
print(bb)
print(c)
print(c_dot)
print(c_dot_2)

f = np.random.random((2,4))
print(f)
print(np.sum(f,axis=1))
print(np.min(f,axis=0))
print(np.max(f,axis=1))



