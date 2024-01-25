# Declare and Assign val to variable

# Integer data type
num = 12345

print("Data Type is: ",type(num))

# String data type
name = 'Nitesh'
print("Data Type is: ",type(name))

# Boolean data type
isTrue = True
print("Data Type is: ",type(isTrue))

# Complex data types
x = 1j
print("Data Type is: ",type(x))

# List Data Type
x = ["apple", "banana", "cherry"]
print("Data Type is: ",type(x))


# tuple Data Type
x = ("apple", "banana", "cherry")
print("Data Type is: ",type(x))

# Range Data Type
x = range(6)
print("Data Type is: ",type(x))

# Dictionary Data Type
x = {"name" : "John", "age" : 36}
print("Data Type is: ",type(x))

# SET Data Type
x = {"apple", "banana", "cherry"}
print("Data Type is: ",type(x))

# Frozenset
x = frozenset({"apple", "banana", "cherry"})
print("Data Type is: ",type(x))

# bytes data types
x = b"Hello"
print("Data Type is: ",type(x))


x = memoryview(bytes(5))
print("Data Type is: ",type(x))