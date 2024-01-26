fruits = ["banana","apple","Oranges","Avocado","Pineapple","Jackfruit"]
filtered_fruit=[]
removed_fruit=[]


def print_result_if_matches_condition():
    for fruit in fruits:
        if "apple" in fruit:
            print(f"I love {fruit}")
            break
        else:
            print(f"I do not love {fruit}")    
            




def append_test():
    for index in range(len(fruits)):
        if 0 == index % 3:
            filtered_fruit.append(fruits[index])
            
    for i in filtered_fruit:
         print(f"Fruint Name: {i}")
        

def remove_test():
    for index in range(len(fruits)):
        if 0 == index % 3:
            fruits.remove(fruits[index])
            
    for i in fruits:
         print(f"Fruint Name: {i}")     
         


         
def test_endswith():
     for fruit in fruits:
        if fruit.endswith('e'):
            print(f"I love {fruit}")
            break
        else:
            print(f"I do not love {fruit}")    
    
                   
            
# print_result_if_matches_condition()   
# filter_if_for()
# remove_test()
test_endswith()