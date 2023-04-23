'''from scipy import constants as cs 
print(cs.liter)
print(dir(cs))'''

'''from scipy.optimize import root 
from math import cos 
def eqn(x): 
  return x+cos(x)
myroot=root(eqn,0)
print(myroot.x)'''

'''from scipy import linalg 
import numpy as np 
a=np.array([[3,2,0],[1,-1,0],[0,5,1]])
b=np.array([2,4,-1])
print(linalg.solve(a,b))''' 

'''from scipy import linalg
import numpy as np 
a=np.array([[1,2],[3,4]])
print(linalg.det(a))''' 

'''from scipy import linalg
import numpy as np 
a=np.array([[1,2],[3,4]])
l,v=linalg.eig(a)
print(l)
print(v)''' 

