#matplotlib
'''import matplotlib.pyplot as plt 
import numpy as np
x1=np.array(['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'])
y1=np.array([ 22.2, 17.6, 8.8, 8, 7.7, 6.7])
mycolor=['r','g','b','magenta','hotpink','black']
plt.bar(x1,y1,color=mycolor)
#plt.barh(x1,y1
plt.grid()
plt.title("popularity of progrrramming languages")
plt.xlabel("programming languages")
plt.ylabel("popularity")
plt.show()'''

'''import numpy as np
import matplotlib.pyplot as plt
# data to plot
n_groups = 5
men_means = (22, 30, 33, 30, 26)
women_means = (25, 32, 30, 35, 29)
# create plot
fig,ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
rects1 = plt.bar(index, men_means, bar_width,color='g',label='Men')
rects2 = plt.bar(index + bar_width, women_means, bar_width,color='r',label='Women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()
plt.show()'''

#dataframe to bar graph
'''from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
a=np.array([[4,8,5,7,6],[2,3,4,2,6],[4,7,4,7,8],[2,6,4,8,6],[2,4,3,3,2]])
df=DataFrame(a, columns=['a','b','c','d','e'], index=[2,4,6,8,10])
df.plot(kind='bar')
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()'''

#stacked bar graph 
'''import matplotlib.pyplot as plt
means_men = (22, 30, 35, 35, 26)
means_women = (25, 32, 30, 35, 29)
groups = ('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5')
fig, ax = plt.subplots()
width = 0.35  # Width of the bars
ind = range(len(means_men))  # X values for the bars
rects1 = ax.bar(ind, means_men, width, label='Men')
rects2 = ax.bar(ind, means_women, width, label='Women', bottom=means_men)
ax.set_ylabel('Scores')
ax.set_title('Scores by Group and Gender')
ax.set_xticks(ind)
ax.set_xticklabels(groups)
ax.legend()
plt.show()'''