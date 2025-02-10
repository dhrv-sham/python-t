# classes are always defined first and then functions are defined

# applying the concept of inheritance
class citizen : 
    def __init__(self,nation,adhar,pan):
        self.nation = nation
        self.adhar = adhar
        self.pan = pan


    def __str__(self):
        return "person is a citizen of " + self.nation  


class person(citizen) : 
    def __init__(self,nation,adhar,pan,name,age,gender):
        super().__init__(nation,adhar=False,pan=False)
        self.name = name 
        self.age =age
        self.gender =gender

    def __str__(self):
        return self.name +" lives in  " + self.nation +  " and "  + super().__str__()


    #  normal class 
class student : 
    # every function has an argument self always in every class 
    def __init__(self, name, standard, phone, gender):
        self.name = name
        self.standard =standard
        self.phone = phone
        self.gender = gender
        
    #custom function 
    def get_name(self) : 
        print(self.name)
        return self.name

    # when an object is printed this function is called
    def __str__(self):
        return "My name is " + self.name + " studying in " + str(self.standard )      



def process(name , standard , phone_number , gender) :
    dhruv = student(name,standard,phone_number,gender)
    print(dhruv.gender)
    print(dhruv)
    print(dhruv.get_name())

    dhruv.name = "dhruv sharma"

    del dhruv.gender

process("dhruv",12, 123456789, "male")
my_entry = person("india",True,True,"dhruv",45,"Male")


print(my_entry)



