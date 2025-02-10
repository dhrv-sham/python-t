class gender : 
    def __init__(self,my_gender):
        self.mygender = my_gender
        


a = 45
b=32
name = "dhruv"
surn_name="sharma"

students = ["dhruv","dev","sharma","shreya"]

for kid in students : 
    print(kid)

my_list = ["dhruv" , 45 , {"reg" : 21703}]
my_set = { "dhruv","dev","sharma","shreya"}
# set inside set using () cant use { }
mixed_Set = {1,2,3 ,(45,656)}
for set_elem in my_set  : 
    if set_elem =="dhruv" : 
        print("we found dhruv !!")
  
    

del my_list[-1]
# print(list(my_list[-1]))
print(my_list.pop())

 
capital=name+" "+surn_name
print(capital.capitalize())

print(name + " "+surn_name)

paid = False

if not paid and (True or False) : 
    print("Congrats you had paid ||")

print(a//b)
print(a%b)
print(a/b)


#  remove duplicates from the list 
numbes = [ 1,23,12,132,1,1,23]
print(numbes)

numbes_unq= list(set(numbes))
print(numbes_unq)
print(str(numbes_unq))

teams=["dhruv","abhay","piyush"]
print(sorted(teams))
print(sorted(teams,reverse=True))


if 132 in numbes : 
    print("yes")


counting = 0  
while counting < 10 : 
    print(counting)
    counting +=1


#  declaring the var type fixed arguments

def defaultFunct(name : str , age: int , gender : gender) : 
    print("Hello " + name + " you are " + str(age) + " old " + "My gender is " + gender.mygender)


# key value pair 
dict = {"name" : "dhruv" , "age" : 45 , "reg" : 21703}

del dict["reg"]

print(str(dict))





tpl = (1,2,3,4,5,6,7,8,9,10)

itr = iter(tpl)

while True : 
    val = next(itr ,None)
    if val is not None : 
        print(val)
        continue
    break


# global
global_val=100

def scope_of_funct () :
    global local_val
    global global_val
    local_val = 50
    global_val = 400
 

scope_of_funct()
print(local_val)
print(global_val)


# giving a variable out of the nested function

def outer_funct() :

    out=100

    def inner_funct() : 
        nonlocal out
        out=200 
    
    inner_funct()
    print(out)    

outer_funct()


# makeing arguments compulsory
male = gender("Male")
defaultFunct("dhruv",45,male)