'''import pandas as pd 
mydataset={ 
    'cars':['Audi',"BMW"],
    'length':[1,2]
}
print(pd.DataFrame(mydataset))'''

'''import pandas as pd 
a=[1,2,3,4]
print(pd.Series(a,index=["a","b","c","d"]))'''

'''import pandas as pd 
data={ 
    'calories':[100,200,300],
    'duration':[5,10,15]
}
f=pd.DataFrame(data)
print(f)
print(f.loc[0])''' 

'''import pandas as pd 
f=pd.read_csv("text1.csv","rt")
print(f.to_string())''' 

'''import pandas as pd 
f=pd.read_json("text1.json")
print(f.to_string())'''

'''import pandas as pd 
f=pd.read_csv("text1.csv")
print(f.head(5))''' 

'''import pandas as pd 
f=pd.read_csv("text1.csv")
final=f.dropna(inplace=True) 
print(final)''' 

'''import pandas as pd
f=pd.read_csv("text1.csv")
final=f.dropna(10,inplace=True)
print(final)''' 

'''import pandas as pd 
f=pd.read_csv("text1.csv")
x=f['categories'].mean()
f['categories'].fillna(x,inplace=Ture)
print(f.to_strinf())''' 

'''import pandas as pd 
f=pd.read_csv("text1.csv")
f['Date']=pd.to_datetime(f['Date'])
print(f.to_string())''' 

'''import pandas as pd
f=pd.read_csv("text1.csv")
print(f.corr())''' 