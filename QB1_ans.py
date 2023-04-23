#Pandas QB 
'''import pandas as pd 
dataframe1={
    'a':[1,2,3,4,5], 
    'b':[5,6,7,8,9]
}
df=pd.DataFrame(dataframe1)

#add index 
print(pd.DataFrame(dataframe1,index=['A','B','C','D','E']))
print(pd.DataFrame(dataframe1))
#display first 3 rows
print(dataframe1.head(3))
#print rows where a is greater than 2
print(df[df['a']>2])
#print rows having value between 2 and 5
print(df[df['a'].between(2,5)])
#calculate mean of a
x=df['a'].mean()
print(x)
#add a row 
df.loc['c']=[1,2]
df=df.drop('c')
#add a column
color=['red','blue','green','violet','maroon']
df['color']=color
#print row having value as 6 in it
print(df.loc[df['b']==6])
#set value to column a specific entry
df.set_value(2,'a',12)
#access particular row
print(df.iloc[0])
#add perfix and suffix
df=df.add_prefix('A_')
df=df.add_suffix('_B') 
print(df)
ser1=pd.Series([1,2,3,4])
ser2=pd.Series([3,4,5,6])
ser_df=pd.DataFrame(ser1,ser2).reset_index()
ser_df=pd.concat([ser1,ser2],axis=1)
print(type(ser_df))'''

#functions QB
#finally block performs cleanup action 
'''def division(a,b): 
  try:
    result = a/b 
    return result 
  except Exception as e: 
    print(e)
  finally: 
    print("finally block")
print(division(1,2))'''
'''import random 
import string 
print("#{:06x}".format(random.randint(0,0xFFFFFF)))
print(random.randint(0,10)*7)
max_length=255 
s=''
#generate random string
for i in range(random.randint(1,max_length)): 
  s=s+random.choice(string.ascii_letters)
print(s)'''
'''
import random 
#generate seeded random number
print(random.Random().random())
#generate random floating pt number 
print(random.random())
'''
#generate random list using random.sample()
'''import random 
population = range(0,50)
numlist=random.sample(population,10)
print(numlist)
no_of_elements=8
print(random.sample(numlist,no_of_elements))'''

#numpy 
#multiplication of two matrices
'''import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[1,2],[3,4]])
print(a*b)'''
#outer product of two vectors 
'''import numpy as np 
a=np.array([[1,0],[0,1]])
b=np.array([[1,2],[3,4]])
print(np.outer(a,b))'''
#determinant of array 
'''import numpy as np 
a=np.array([[1,2],[3,4]])
print(np.linalg.det(a))'''
#sum of diagonal elements  
'''import numpy as np
a=np.array([[1,2],[3,4]])
print(np.trace(a))'''
#reverse a array
'''
import numpy as np
a=np.array([1,2,3,4])
print(a[::-1])''' 
#np.asarray is used to convert list or tuple to array 
#checkboard pattern 
'''import numpy as np 
x=np.ones((3,3))
x=np.zeros((8,8),dtype=int) 
x[1::2,::2]=1
x[::2,1::2]=1
print(x)'''
#random 5x5 matrix 
'''import numpy as np
x=np.zeros((5,5))
x=x+np.arange(5)
print(x)'''

#file handling 
#count number of line in file 
'''def file_length(f1): 
  with open(f1) as x:
    for i,l in enumerate(x):
      pass 
    return i+1 
print("no of lines:",file_length("filename.txt"))'''
#count number or words in file 
'''def count_words(filepath):
 with open(filepath) as f:
  data = f.read()
 data.replace(",", " ")
 return len(data.split(" "))
print(count_words("words.txt"))'''


#combine two dataframes - print(df1.combine_first(df2))
#combine two dataframes with keys - merge(df1,df2,on=['key1','key2'])