## Functions Assignment
#Name:
#Date:


#Task 1.
#Create a function that takes in two numbers
#and determines if both are greater than 10. Return True or False
#in: two numbers
#do: determine if both numbers are greater than 10
#out: True or False

def two_ten(num1, num2):
    if num1 > 10 and num2 > 10: return True
    else: return False

print("Testing two_ten")
print(two_ten(3, 4) == False)
print(two_ten(11, 12) == True)
print(two_ten(5, 11) == False)
print(two_ten(111, 1) == False)

#Task 2.
#A grocery list has 10 spaces for items.
#Given a list, determine if it is full or not. Empty spaces are ' '.
#in: list
#do: determine if it it is full
#out: True or Fals

groc = ['banana', 'lettuce', ' ', ' ', ' ']

def list_full(lst):
    if lst.count(' ') == 0:
        return True
    else: return False

print('Testing list_full')
print(list_full(["a", "b", "c"]) == True)
print(list_full([" ", 'b', 'c']) == False)

#Task 3.
#To add to the grocery list, the user gives
#an item and the position on the list to add it.
#if there is already something in that position, overwrite it.
#in: grocery list (list), item to add (string), position to add (int)
#do: changed list
#out: None

def add_groc(lst, item, pos):
    pass



#Task 4.
#Ask the user the name of the store they will shop at.
#Change the value of the GLOBAL variable storeName
#in: None
#do: ask for user input, get store name, change storeName variable
#out: None

storeName = '' #global variable

def get_Store():
    pass

get_Store()  #give it  "Superstore"
print(storeName == "Superstore")






