# Inserting elements at the beginning using update method
test_dict = {"Gfg" : 5, "is" : 3, "best" : 10}
 
updict = {"pre1" : 4, "pre2" : 8}

updict.update(test_dict)
 
print(f"The required dictionary : {updict}")