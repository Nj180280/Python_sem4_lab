#list 
'''emp=["John",213,"Manager"]
print("name:%s , id:%d , pos:%s" %(emp[0],emp[1],emp[2]))
lst2=[1,2,3,4,5]
# print(lst2[1:4])
# print(lst2[:])
# print(lst2[0:])
# print(lst2[:4])
# print(lst2[:-1])
# print(lst2[-1:-3])
# print(lst2[:-3])
# print(lst2[-3:-1])

lst3=lst2*2 #repetation 
print(lst3)
lst4=lst2+lst3 #concatenation 
print(lst4)
print(len(lst4)) #length 
print(5 in lst4) #membership ''' 

#adding and removing elements in list 
'''lst1=[]
n=int(input("how many elements to add:"))
for i in range(0,n): 
    lst1.append(int(input("Enter element:")))
n1=int(input("enter element to remove:"))
if(n1 in lst1): 
    lst1.remove(n1)
    print(lst1)
else:
    print("element not found")
print(lst1)'''

#tuple 
'''tup=(1,2,"Hello")
tup2=(4,5,"World")
tup3=tup+tup2 
# print(tup3[1:3])
# print(tup3)
# print(tup)
print (min(tup2,tup3))
print (max(tup2,tup3))'''

#dictionary 
'''dict={"Name":"Niranjan","Class":"SE","RollNo":47}
print(dict['Name'])
print(dict['Class'])
print(dict['RollNo'])
dict2=dict.fromkeys("Hello") 
print(dict.items()) '''

#dictionary input 
'''n=int(input("enter number of elements:"))
dict={}
for i in range(n): 
    key=input("enter key:")
    value=input("enter value")
    dict[key]=value 
print(dict)''' 

#string 
name="niranjan"
age=19 
a1="My name is {0} and I am {1} now"
print(a1.format(name,age))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.count("a"))
print(name.casefold())
print(name.index("a"))
print(name.split("r"))
print(name.replace("a","A"))