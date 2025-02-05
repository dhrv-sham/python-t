def attach_surname ( name , surname ) :
    print(name + " " +  surname) 
    return name + " " +   surname

def random_funct(a , b) :
    return a + b

def arb_args(*args) :
    print(args[1])
    return args[1] 
    
print(arb_args(34,23,12))    
print(random_funct(5,9))
print("full name : " + attach_surname("dhruv","sharma"))