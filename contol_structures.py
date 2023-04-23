#square 
'''for i in range(1,6): 
    for j in range(1,6): 
        print("*",end='')
    print(" ")''' 

#right angled triangle 
'''for i in range(1,6): 
    for j in range(1,i+1): 
        print("*",end="")
    print(" ")''' 

#complete triangle 
'''n = int(input("Enter the height of the triangle: "))
# Loop to print the complete triangle
for i in range(n):
    # Print spaces before asterisks
    for j in range(n - i - 1):
        print(" ", end="")
    # Print asterisks
    for k in range(2 * i + 1):
        print("*", end="")
    # Move to the next line
    print()''' 

#factorial 
'''n=int(input("enter number to find factorial of:"))
fact=1
for i in range(1,n+1): 
    fact=fact*i 
print(fact)''' 

#armstrong 
'''n=int(input("enter number to check armstrong for:"))
sum=0
b=n
while(n!=0): 
    a=n%10 
    sum=sum+a**3
    n=n//10 
if(b==sum): 
    print("YES")
else: 
    print("NO")''' 

#armstrong print till given limit 
'''n = int(input("Enter any number: "))
for n in range(1, n+1):
    sum = 0
    b = n
    while(n != 0):
        a = n % 10
        sum = sum + a**3
        n = n // 10
    if b == sum:
        print(b)''' 

#sum of natural numbers 
'''n=int(input("enter  till what number you need sum:"))
summ=0
for i in range(1,n+1): 
    summ=summ+i 
print(summ)''' 

#sum of digits 
'''n=int(input("enter any number"))
b=n 
for n in range(1,n+1): 
    summ=0 
    while(n!=0): 
        a=n%10 
        summ=summ+a 
        n=n//10 
print(summ)''' 

#reverse a number 
'''n=int(input("enter any number:"))
rev=0
while(n!=0): 
    a=n%10 
    rev=rev*10+a 
    n=n//10
print(rev)''' 

#fibonacci series 
'''n=int(input("how many terms need to be printed:"))
n1=0
n2=1
c=0
while(n>c): 
    print(n1)
    temp=n1+n2 
    n1=n2 
    n2=temp 
    c+=1'''
