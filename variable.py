import random

#  str (can be represneted by "" , ''), int ,  float ,complex ,Collections ( dict , list , tuple ,  set ), bool (True ,False)
#  stores the complex values real and imaginary numbers
# unlike in java we can stores difrrent type of data var in the list  
compl = 1j+5 
print(type(compl))

expo_value = 10e4 #(aeb) means a^b

# main difference between list and tuple is tuple is imutable
# list and tuple 
my_list= ["dhruv" , 45 , 56 , True]
z=list([45,43,23,"dhruv sharma"])
my_list.append(100)
for elements in my_list : 
    if str(elements) == "56" : 
        print("caught")

# tuple ()
# list []
y = tuple((45,"dhruv sharma"))
print(y)

# dictionary {}
dictionary = dict({"name" : "dhruv sharma" , "age" : 45})
x={"name" : "dhruv sharma" , "age" : 45}
print(x["name"])
print(dictionary)

#  set and frozn set have same functionality to stores the unique elements but frozen sets are immutable 
my_elements = set({"apple" ,"banana" , "orange"})
my_frozen_elements =  frozenset({"apple" , "banana" , "orange"})



#  range [1,4,7,10]
my_range  =  range(1, 10, 3)
print(random.randint(5,10))


# type conversions
print(int(14.9)) # 14 
print(float(14)) # 14.0

# for the multiline string 
x  = """ hello my name is dhruv,
 sharma we are very good players """
print(x)




