my_string = "Hello, Python!"

# Print the Original String
print("Original String: ", my_string)


#String concatenation
print("Concatenated String: ", my_string + " Welcome")

#Print String length
print("Length of String: ", len(my_string))

# Accessing individual characters in a string

first_char = my_string[0]
second_char = my_string[1]

print("First Char: ",first_char)
print("Second Char: ",second_char)
print("Last Char: ", my_string[-1])

# Substring using slicing
print("String slicing: ", my_string[0:5])
print("String slicing: ", my_string[-7:-1])

# String repetation

print("  " , my_string * 2)

# String formatting

name="Nitesh"
age=32
formatted_string=f"My name is {name} and I am {age} years old"

print("Formatted String: ",formatted_string)