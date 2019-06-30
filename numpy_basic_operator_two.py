import numpy as np

A = np.arange(2,14).reshape((3,4))
# 求最小值的索引
print(np.argmin(A))

print(np.argmax(A))
# 求平均值
print(np.mean(A))
print(A.mean())
print(np.average(A))
# 求中间值
print(np.median(A))
# 求累加
print(np.cumsum(A))
# 求累差
print(np.diff(A))
# 找出非0的数的index
print(np.nonzero(A))
# 排序,排完默认升序
B = np.arange(14,2,-1).reshape((3,4))
print(np.sort(B))

# 行转列,列转成行
print(np.transpose(A))
print((A.T).dot(A))
#所有小于5的都赋值为5，所有大于9的都赋值为9，介于5和9之间的保持不变
print(np.clip(A,5,9))
# 列的平均值计算
print(np.mean(B, axis=0))
