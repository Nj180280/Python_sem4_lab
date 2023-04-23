#classes
'''class dog: 
    attr="Mammal" 
    def __init__(self,name): 
        self.name=name 
    def speak (self): 
        print("Dog barks")
obj1=dog("Rodger") 
obj1.speak()'''

#inheritance
'''class mammal: 
    def speak(self): 
       print("mammal can speak")
class human(mammal): 
    def attri(self): 
        print("human is a mammal")
class sapiens(human): 
    def sap(self): 
        print("sapiens is human and mammal both")
sapi=sapiens()
sapi.speak()
sapi.attri()
sapi.sap()'''

#polymorphism 
#method overloading 
'''class Addition:
	# first sum for 2 params
	def my_sum(self, a, b):
		return a + b
	# second overloaded sum for 3 params
	def my_sum(self, a, b, c):
		return a + b + c
obj=Addition()
obj.my_sum(1,2)
obj.my_sum(3,4,5)'''

#method overriding
'''class Shape:
    data1 = "abc"
    def no_of_sides(self):
        print("My sides need to be defined. I am from shape class.")
    def two_dimensional(self):
        print("I am a 2D object. I am from shape class")
class Square(Shape):
    data2 = "xyz"
    def no_of_sides(self):
        print("I have 4 sides. I am from Square class")
    def color(self):
        print("I have teal color. I am from Square class.")
sq = Square()
sq.no_of_sides()
sq.two_dimensional()
sq.color()
print("Old value of data1 = ", sq.data1)
sq.data1 = "New value"
print("The value of data1 in Shape class overridden by the Square class = ", sq.data1)''' 

#operator overloading 
'''class example:  
    def __init__(self, X):  
        self.X = X  
    # adding two objects  
    def __add__(self, U):  
        return self.X + U.X  
object_1 = example( int( input( print ("Please enter the value: "))))  
object_2 = example( int( input( print ("Please enter the value: "))))  
print (": ", object_1 + object_2)  
object_3 = example(str( input( print ("Please enter the value: "))))  
object_4 = example(str( input( print ("Please enter the value: "))))  
print (": ", object_3 + object_4)'''


