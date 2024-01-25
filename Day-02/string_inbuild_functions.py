arn = 'arn:aws:iam::123455679856477:user/johndoe'

list1=arn.split("/")[0]
list2=arn.split("/")[1]

print(list2)

#String Handling Functions
print("Name in Upper Case: ",list2.upper())

print("Length of String:  ",len(arn))

# Remvoe spaces 

str = "     There are spaces bfore and after and remove those    "
print(str.strip())