'''import matplotlib.pyplot as plt 
import numpy as np 
a=np.array([0,0])
b=np.array([100,200])
plt.plot(a,b)
plt.show()'''

'''import matplotlib.pyplot as plt 
import numpy as np 
a=np.array([0,10])
b=np.array([20,30])
plt.plot(a,b,'o')
plt.show()''' 

'''import matplotlib.pyplot as plt
import numpy as np
a=np.array([0,1,2])
plt.plot(a,marker='o',ms=15,mec='g',mfc='r',linewidth=5,linestyle='dotted')
plt.show()'''

'''import matplotlib.pyplot as plt
import  numpy as np 
x1=np.array([0,1,2,3])
y1=np.array([4,5,6,7])
x2=np.array([1,2,3,4])
y2=np.array([5,6,7,8])
plt.plot(x1,x2,y1,y2,marker='*',ms=5,mfc='b',mec='r',linestyle='dotted')
font1={'family':'serif','color':'blue','size':'10'}
font2={'family':'serif','color':'blue','size':'10'}
plt.xlabel("X axis",fontdict=font1)
plt.ylabel("Y axis",fontdict=font2)
plt.title("Two line graph",loc='center')
plt.grid(color='g',linestyle='dotted')
plt.show()''' 

'''import matplotlib.pyplot as plt 
import numpy as np
x1=np.array([1,2,3,4])
y1=np.array([2,3,4,5])
x2=np.array([3,4,5,6])
y2=np.array([4,5,6,7])
x3=np.array([5,6,7,8])
y3=np.array([6,7,8,9])
plt.subplot(1,3,1)
plt.plot(x1,y1)
plt.title("Plot 1",color='b')
plt.show()

plt.subplot(1,3,2)
plt.plot(x2,y2)
plt.title("Plot 2",color='b')
plt.show()

plt.subplot(1,3,3)
plt.plot(x3,y3)
plt.title("Plot 3",color='b')
plt.show()'''

'''import matplotlib.pyplot as plt
import numpy as np
x1=np.array([1,2,3])
y1=np.array([2,3,4])
x2=np.array([4,5,6])
y2=np.array([6,7,8])
plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.show()
plt.show()'''

'''import matplotlib.pyplot as plt 
import numpy as np
a=np.array([1,2,3])
b=np.array([3,2,1])
#we can also use barh and barv to plot horizontal and vertical bar graph
plt.bar(a,b,color='r',width=0.5)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Bar Graph")
plt.grid()
plt.show()'''

'''import matplotlib.pyplot as plt 
import numpy as np 
x=np.random.normal(170,10,250)
plt.hist(x,color='b')
plt.show()'''

'''import matplotlib.pyplot as plt 
import numpy as np 
a=np.array([10,20,30,40])
mylabels=['A','B','C','D']
mycolors=['red','magenta','black','hotpink']
myexplode=[0,0,0,0.1]
plt.pie(a,labels=mylabels,startangle=90,explode=myexplode,shadow=True,colors=mycolors) 
plt.legend(title="Pie Chart")
plt.show()'''