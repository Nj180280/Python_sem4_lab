'''def func1(num1,num2): 
    ans=num1+num2
    return ans 

print(func1(2,3))''' 

#lambda function 
'''def myfunc(n): 
    return lambda a:a*n 

double=myfunc(2)
triple=myfunc(3)
print(double(11))
print(triple(11))''' 

#recursion 
'''def fact(n): 
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))'''

'''def summ(n): 
    if n==0: 
        return 0 
    else: 
        return n+summ(n-1)
print(summ(5))'''

'''def fibo(n): 
    if n==0: 
        return 0 
    if n==1 or n==2: 
        return 1
    else: 
        return fibo(n-1)+fibo(n-2)
for i in range(5): 
    print(fibo(i))'''

