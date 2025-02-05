# python tutorials starts from here 
import sys

# defining a function
_global_var = "this is a global variable "
def myFunct() : 
    _global_var = "local var"
    global variable 
    variable = "making  a global variable"
    print(_global_var)#local
    

print(_global_var)#global

myFunct()

print(_global_var)#global

print(variable)




print("version of the system is " , sys.version)
print ("Hello world")

name = "dhruv sharma"
age = 30

if 5 > 2: 
    print("5 is greater than 2")
    
# type conversion
# will be treated as int  
price = int(45)
dollars=float(45)
api=str(100)

#  type check of a variable 
print(type(price))
print(type(dollars))
print(type(api))


_my_reg_nu3="21bce0703"


#  various name casing 
# camel case 
myVarName="dhruv sharma"

# pascal case 
MyVarName = "dhruv sharma"

# snake case 
my_var_name ="dhruv sharma"

#  assign multiple var with differnet var in a single go
first , second , third = "dhruv" , "dev" , "arvind"


# assign same value to differnet values 

a = b = c =10

print(first,"\n",second,"\n",third)

print(a+b+c)

#  extracting the collection directly
fruits = ["orange" , "watermelon" , "guavava" , "apple"]

x,y,z,last=fruits

print(fruits)
print(last)
