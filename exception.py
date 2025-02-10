import json

my_api= '{"name" : "dhruv sharma" , "age" : "31" , "city" : "bengaluru"}'
data_dict = json.loads(my_api)
data_json=json.dumps(data_dict)

print(data_json)

print(data_dict["name"])


def excetion_handling(numbA : int , numbB : int) :
    try : 
        result = numbA / numbB
        print(result)
        if numbA == numbB : 
            raise ValueError("Both numbers are same")

    except ZeroDivisionError as e : 
        print(e)  
    except : 
        print("Something went wrong " )
    else : 
        print("Division is successful")
    finally : 
        print("End of the program where numba is : ", numbA, " and numbB is : ", numbB)        





# excetion_handling(10,0)

# excetion_handling(10,10)


# excetion_handling(10,5)