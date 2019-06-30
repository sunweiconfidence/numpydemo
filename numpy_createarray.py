import numpy as np
a = np.ones((3,4),dtype=np.int16)
print(a)
print('number of dim:',a.ndim)

b = np.arange(10,20,2)
print(b)

c = np.arange(12).reshape((3,4))
print(c)

d = np.linspace(1,10,20)
print(d)

e = np.linspace(1,10,6).reshape((2,3))
print(e)