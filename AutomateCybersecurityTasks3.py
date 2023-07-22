#STRING OPERATORS 
#str() function = converts the input object into a string 
new_string = str(123)
print(type(new_string)) #class string 

#len() function = tells us how many characters are in an object
# returns the number of elements in an object 
print(len("Hello")) # 5 = each for one letter in the word

#string concatenation 
print("Hello" + "world") #Helloworld

#String methods
# a method is a function that belongs to a specific data type 
# common string methods are .upper and .lower
# .upper() returns a copy of string in uppercase letters
print("Hello".upper()) #HELLO 
print("Hello".lower()) #hello


#String indices and slices

#index is number assigned to every element in a sequence that indicates its position
"Hello" # H = index 0, E = index 1 ....
"Hello"[1] # outputs "E"

#We can extract a larger part of a string by specifing more indices 
#it is called SLICE 
"Hello"[1:4] #starts at 1 ands at 3 (output is "ell")

#.index() method
#finds the first occurrence of the input in a string and returns its location 
#exercise
#we want to find the letter E in Hello string 
print("HELLO".index("E")) #STRINGS IN PYTHON ARE CASE SENSITIVE
#returns 1 because E has a index number of 1
print("HELLO".index("L")) #2
#method only identifies the first occurence in "HELLO" and not the second

#Strings are immutable 
#meaning we cannot make changes like this 
my_string = "Hello"
my_string[1] = "A" #error = strings cannot be changed like this 


#More on strings 
#Indices 
#An index is a number assigned to every element in a sequence that indicates its position.
# h 3 2 r b 1 7 
# 01234567891011

#Bracket notation
#Bracket notation refers to the indices placed in square brackets. 
#You can use bracket notation to extract a part of a string.
device_id = "h32rb17"
print("h32rb17"[0])
print(device_id[0])
#You can also take a slice from a string. 
#When you take a slice from a string, you extract more than one character from it.
print("h32rb17"[0:3])

#String functions and methods
#The str() and len() functions are useful for working with strings. 
#You can also apply methods to strings, including the .upper(), .lower(), and 
#.index() methods. A method is a function that belongs to a specific data type.

#str() and len()
#The str() function converts its input object into a string. 
#Consider the example of an employee ID 19329302 that you need to convert into a string.
string_id = str(19329302)

#the len() function, which returns the number of elements in an object.
device_id_length = len("h32rb17")
if device_id_length == 7:
    print("The device ID has 7 characters.") 
#the device has 7 characters

#.upper() and .lower() 
#The .upper() method returns a copy of the string with all of its characters in uppercase.
"Information Technology".upper() #"INFORMATION TECHNOLOGY"

#.lower() method returns a copy of the string in all lowercase characters.
"Information Technology".lower() #"information technology"

#.index()
#The .index() method finds the first occurrence of the input in a string and returns its location.
print("h32rb17".index("r"))

#when input may not be found, Python returns error 
#if a string contains more than one instance of a character, only the first one will be returned.
print("r45rt46".index("r")) prints only 0

#Finding substrings with .index()
tshah_index = "tsnow, tshah, bmoreno - updated".index("tshah")
print(tshah_index)
#When using the .index() method to search for substrings, you need to be careful.
#In the previous example, you want to locate the instance of "tshah". 
#If you search for just "ts", Python will return 0 instead of 7 because "ts" 
#is also a substring of "tsnow". 


#Python activity
employee_id = 4186
print(type(employee_id)) #int 
employee_id = str(4186)
print(type(employee_id)) #string 

#conditional statement that displays a message if the length of the employee ID is less than five digits
employee_id = 4186
employee_id = str(employee_id)
employee_id_length = len(employee_id)
if employee_id_length < 5:
    print("This employee ID has less than five digits. It does not meet length requirements.")
    
 
#Write an if statement that evaluates whether the length of employee_id is less than 5.
#reassign employee_id by concatenating "E" in front of the four-digit employee ID
employee_id = 4186
employee_id = str(employee_id)
print(employee_id)

employee_id_length = len(employee_id)

if employee_id_length < 5:
    employee_id = "E" + employee_id
print(employee_id)

# Extract the fourth character in `device_id` and display it
device_id = "r262c36"
print(device_id[4])

# Extract the first through the third characters in `device_id` and display the result
device_id = "r262c36"
print(device_id[0:3])

# Assign `url` to a specific URL
url = "https://exampleURL1.com"
# Extract the protocol of `url` along with the syntax following it, display the result
print(url[0:8]) #https://
print(url[8:25]) #exampleURL1.com

# Display the index where the domain extension ".com" is located in `url`
url = "https://exampleURL1.com"
print(url.index(".com")) #19

url = "https://exampleURL1.com"
# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url` 
ind = url.index(".com")
# Extract the website name in `url` and display it
print(url[8:25])



#List operations in Python 
#List is another data type in Python 
my_list = ["a", "b", "c", "d", "e"]
print(my_list[1]) #= "b"

#List concatenation 
#Combining two lists into one by placing the elements of the second list after first list
my_list1 = ["a", "b", "c", "d", "e"]
my_list2 = ["a", "b", "c", "d", "e"]
print(my_list1 + my_list2) #["a", "b", "c", "d", "e", "a", "b", "c", "d", "e"]

#Difference between lists and strings
#strings are immutable 
#lists can be changed, they are immutable 
#Change a specific element in a list 
my_list3 = ["a", "b", "c", "d", "e"]
my_list3[1] = 7 #["a", 7, "c", "d", "e"]

#Methods for strings 
#.insert() method = adds an element in a specific position inside a list 
my_list4 = ["a", "b", "c", "d", "e"]
my_list4.insert(1,7) #1, is a position in index we want to input
print(my_list4)      #7 is what we want to input into our list 
                     #["a", 7, "b", "c", "d", "e"] = "b" is shifted by 1 position
                     #7 is inputted into position of "b"

#.remove() method = removes the first occurence of a specific element in a list 
my_list5 = ["a", "b", "c", "d", "e"]
#remove method removes the first instance 
my_list5.remove("d") #["a", "b", "c", "e"] = "d" is removed from the string 


#Write a simple algorith
#An algorith is a set of rules that solve a problem

#Exploring first algorithm
#List of IP addresses
IP = ["198.567.xx.xx", "198.501.xx.xx", "180.644.xx.xx", "192.668.xx.xx", "184.690.xx.xx"]

#solving this problem with one algorithm with one IP address
address = "198.567.xx.xx"
# Extract the first three characters of an IP address
print(address[0:3])
#Now we can solve this problem for one IP address we can put it into a loop and solve it for more

#.append() method adds input to the end of the list 
networks = []
for address in IP: #as a code runs every address will be stored temporarly in address variable
    networks.append(address[0:3])#we append the temporarly variable in address variable to add an item to the networks list
print(networks)

#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#Lists and the security analyst
#List data is a data structure that consists of a collection of data in sequential form. 
#You can use lists to store multiple elements in a single variable. A single list can contain multiple data types. 

#Working with indices in lists
#Like strings, you can work with lists through their indices, and indices start at 0. In a list, an index is assigned to every element in the list.
listt = ["elarson", "fgarcia", "tshah", "sgilmore"]:
#          0            1         2         3

#Bracket notation
#Similar to strings, you can use bracket notation to extract elements or slices in a list
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
print(username_list[2])
print(["elarson", "fgarcia", "tshah", "sgilmore"][2])  #these funciton the same

#Extracting a slice from a list
##Just like with strings, it's also possible to use bracket notation to take a slice from a list.
#When you extract a slice from a list, the result is another list. This extracted list is called 
#a sublist because it is part of the original, larger list. 
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
print(username_list[0:2]) 
#output is ['elarson', 'fgarcia']

#Changing the elements in a list
#Unlike strings, you can also use bracket notation to change elements in a list.
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
print("Before changing an element:", username_list)
username_list[1] = "bmoreno"
print("After changing an element:", username_list)
#output
#Before changing an element: ['elarson', 'fgarcia', 'tshah', 'sgilmore']
#After changing an element: ['elarson', 'bmoreno', 'tshah', 'sgilmore']


#List methods
#List methods are functions that are specific to the list data type. 
#These include the 
#.insert()
#.remove()
#.append()
#.index()

## .insert() 
#The .insert() method adds an element in a specific position inside a list. 
#It has two parameters. 
#The first is the index where you will insert the new element, 
#and the second is the element you want to insert.
username_list = ["elarson", "bmoreno", "tshah", "sgilmore"]
print("Before inserting an element:", username_list)
username_list.insert(2,"wjaffrey")
print("After inserting an element:", username_list)
#['elarson', 'bmoreno', 'wjaffrey', 'tshah', 'sgilmore']

## .remove()
#The .remove() method removes the first occurrence of a specific element in a list. 
#It has only one parameter, the element you want to remove.
username_list = ["elarson", "bmoreno", "wjaffrey", "tshah", "sgilmore"]
print("Before removing an element:", username_list)
username_list.remove("elarson")
print("After removing an element:", username_list)
#['bmoreno', 'wjaffrey', 'tshah', 'sgilmore']
#This code removes "elarson" from the list. The elements that follow "elarson" 
#are all shifted one position closer to the beginning of the list.

#.append() 
#The .append() method adds input to the end of a list. 
#Its one parameter is the element you want to add to the end of the list. 
username_list = ["bmoreno", "wjaffrey", "tshah", "sgilmore"]
print("Before appending an element:", username_list)
username_list.append("btang")
print("After appending an element:", username_list)
#['bmoreno', 'wjaffrey', 'tshah', 'sgilmore', 'btang']
#Places "btang" at the end of the username_list

#The .append() method is often used with for loops
#to populate an empty list with elements. 
#You can explore how this works with the following code:
numbers_list = []
print("Before appending a sequence of numbers:", numbers_list)
for i in range(10):
    numbers_list.append(i)
print("After appending a sequence of numbers:", numbers_list)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

## .index()
#Similar to the .index() method used for strings, the .index()
username_list = ["bmoreno", "wjaffrey", "tshah", "sgilmore", "btang"]
username_index = username_list.index("tshah")
print(username_index)
# 2
#Because the index of "tshah" is 2, it outputs this number.

#Algorithm exercise
#There's a new employee joining the organization, and they need to be provided 
#with a username and device ID. In the following code cell, you are given a username and device ID
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]
print(approved_users)
print(approved_devices)
#['elarson', 'bmoreno', 'tshah', 'sgilmore', 'eraab']
#['8rp2k75', 'hl0s5o1', '2ye3lzg', '4n482ts', 'a307vir']
new_user = "gesparza"
new_device = "3rcv4w6"

approved_users.append(new_user)
approved_devices.append(new_device)
print(approved_users)
print(approved_devices)
#['elarson', 'bmoreno', 'tshah', 'sgilmore', 'eraab', 'gesparza']
#['8rp2k75', 'hl0s5o1', '2ye3lzg', '4n482ts', 'a307vir', '3rcv4w6']

#An employee has left the team and should no longer have access to the system. 
#In the following code cell, you are given the username and device ID of the user to be removed
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir", "3rcv4w6"]
print(approved_users)
print(approved_devices)
#['elarson', 'bmoreno', 'tshah', 'sgilmore', 'eraab', 'gesparza']
#['8rp2k75', 'hl0s5o1', '2ye3lzg', '4n482ts', 'a307vir', '3rcv4w6']
removed_user = "tshah"
removed_device = "2ye3lzg"

approved_users.remove(removed_user)
approved_devices.remove(removed_device)
print(approved_users)
print(approved_devices)
#['elarson', 'bmoreno', 'sgilmore', 'eraab', 'gesparza']
#['8rp2k75', 'hl0s5o1', '4n482ts', 'a307vir', '3rcv4w6']

#As part of verifying a user's identity in the system, you'll need to check 
#if the user is one of the approved users.
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
    
username = "sgilmore" 

if username in approved_users:
    print("The user", username ,"is approved to access the system")
else:
    print("The username", username, "is not approved to access the system.")

#The user sgilmore is approved to access the system
#The username Vicky is not approved to access the system.


#find the index of username in the approved_users
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"
ind = approved_users.index(username)
print(ind)
# 2


#find an index in one list and then use this index to display connected information in another list
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
username = "sgilmore"
ind = approved_users.index(username) # 2
# Display the device ID at the index that matches the value of `ind` in `approved_devices`
print(approved_devices[ind]) # checks the number of index 2 to devices index 2 and outputs it 


#creating the algorithm is to determine if a username and device ID correspond.
#conditional that checks if the username is an element of the approved_devices 
#and if the device_id stored at the same index as username matches the device_id entered
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"
device_id = "4n482ts"
ind = approved_users.index(username)

# Conditional statement
# If `username` belongs to `approved_users`, and if the device ID at `ind` in `approved_devices` matches `device_id`,
# then display a message that the username is approved,
# followed by a message that the user has the correct device
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"
device_id = "4n482ts"
ind = approved_users.index(username)

if username in approved_users and device_id == approved_devices[ind]:
    print("The username", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)
#The username sgilmore is approved to access the system.
#4n482ts is the assigned device for sgilmore

#It would also be helpful for users to receive messages when their username is not approved or their device ID is incorrect.
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"
device_id = "4n482ts"
ind = approved_users.index(username)

if username in approved_users and device_id == approved_devices[ind]:
    print("The user", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)

elif username in approved_users and device_id != approved_devices[ind]:
    print("The user", username, "is approved to access the system, but", device_id, "is not their assigned device.")

#The user sgilmore is approved to access the system.
#4n482ts is the assigned device for sgilmore
#OR 
#The user sgilmore is approved to access the system, 
#but 4n482s is not their assigned device.

