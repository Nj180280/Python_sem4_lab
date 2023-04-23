#arrays 
'''import array as arr 
a=arr.array('d',[1,2,3,4])
b=arr.array('d',[3.2,4.3])
c=arr.array('d')
c=a+b
print(c)''' 

'''import numpy as np 
a=np.array([1,2,3,4]) #1D array
b=np.array([[1,2,3,4],[5,6,7,8]]) #2D array 
c=np.array([[[1,2,4,5],[6,7,8,9]],[[1,3,5,7],[2,4,6,8]]])
print(c.ndim)
print(c)
d=np.array([1,2,3,4,5],ndmin=5)
print(d.ndim)
print(c[0,0,1])
e=np.array([1,2,3],dtype='S')
print(e)''' 

'''import numpy as np 
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a.shape)
b=np.array([1,2,3,4,5,6])
print(b.reshape(3,2)) #2d array
print(b.reshape(3,2,1)) #3d array 
for x in np.nditer(a): 
    print(x)''' 

'''import numpy as np 
a=np.array([1,2,3,4,6])
print(a.searchsorted(5))
b=np.array([[1,3,2],[6,5,4]])
print(np.sort(b))'''

