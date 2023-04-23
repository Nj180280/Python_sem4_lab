#try,else,except,finally
try: 
    num=10 
    den=0 
    #a=[1,2,3]
    #print(num/den)
    print("hello")
except ZeroDivisionError : 
    print("cannot be divided")
except IndexError: 
    print("index exceeded")
else:
    print("else is working")
finally: 
    print("this always works")