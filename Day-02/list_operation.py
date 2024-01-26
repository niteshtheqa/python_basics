mylist = ["apple", "banana", "cherry"]

print("List: ", mylist)

print("Length of List: ", len(mylist))

# List with different Data Types

list1 = ["abc", 34, True, 40, "male"]

print("List with different data types: ", list1)

# Creating list using Contructor

thisList = list(("apple", "banana", "mango"))

print("Print list : ", thisList)


def list_iterations():
    for fruit in mylist:
        print(fruit)


def print_list_comprehension():
    print("\n\n\nUsing comprehension")
    [print(item) for item in mylist]


def using_while_loop():
    print("\n\n\nUsing while loop")
    index = 0
    while index < len(mylist):
        print(mylist[index])
        index += 1


def using_map_function(item):
    print(item)


def check_if_item_is_exists():
    if "APPLE".lower() in mylist:
        print("Yes, 'apple' is in the fruits list")


def change_list():
    mylist[4:7] = ["watermenlon"]
    print(mylist)
    
    
def insert_item_at_position():
    mylist.insert(1,"Broccoli")
    print(mylist)    
    
# list_iterations()

# print_list_comprehension()

# using_while_loop()

# print("\n\n\nUsing map function")
# list(map(using_map_function, mylist))


# check_if_item_is_exists()
# change_list()
insert_item_at_position()


         