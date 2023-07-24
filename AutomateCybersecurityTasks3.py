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

#To complete this task, you must define a function named login that takes in two parameters, username and device_id
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Define a function named `login` that takes in two parameters, `username` and `device_id`
def login(username, device_id):

    if username in approved_users:
        print("The user", username, "is approved to access the system.")
        
        ind = approved_users.index(username)
        if device_id == approved_devices[ind]:
          print(device_id, "is the assigned device for", username)
        else:
          print(device_id, "is not their assigned device.")

    else:
        print("The username", username, "is not approved to access the system.")

login("elarson", "8rp2k75")
#first response
#The user elarson is approved to access the system.
#8rp2k75 is the assigned device for elarson
#Second response
#The user elarson is approved to access the system.
#8rp2k7 is not their assigned device.
#Third response
#The username elason is not approved to access the system.



###Regular expressions in Python 
#they are used to search for patterns in a strings 
#is a sequence of characters that form a pattern, we can use thom to search in file
# + represents one or more occurrences of a specific character 
#=regular expressions allow us to search for a string of characters 
#"a+" searches for a matches - it could be "a" "aa" "aaa" even thousand a occurences
"Device IDs"
"a37rz87" #a
"io2aap4" #aa
"32rb5a2" #a
"9aaa95y" #aaa
#regular expressions would return list ["a", "aa", "a", "aaa"]

#\w
#matches with any alphanumeric character but it doesnt match symbols

#\w and + sign
#"\w" matches any alphanumeric character, and the 
# + plus sign matches any number of occurrences of the character before it.
#"\w+" matches
"192"
"abc123"
"security"

#we can use these to extract an email address from a log 
"user1@email1.com"
#\w+ @ \w+ \. \w+
#this will exclude everything in our string except our specified email addresses

#extract eemail addresses
#findall() function 
#returns a list of matches to regular expression 
import re
email_log = """Email recieved June 2 from user1@email.com.
Email recieved June 2 from user2user2@email.com.
Email rejected June 2 from invalid_user3@email.com.
"""
#returns a list of matches of a regular expression 
print(re.findall("\w+@\w+\.\w+",email_log))
#the second argument indicates where to search for the pattern



#More about regular expressions
#Basics of regular expressions
#A regular expression (regex) is a sequence of characters that forms a pattern.
#To access regular expressions and related functions in Python, 
#you need to import the re module first.
import re
#Regular expressions are stored in Python as strings. 
#Then, these strings are used in re module functions to search through other strings.
#There are many functions in the re module(we will use re.findall())
#The re.findall() function returns a list of matches to a regular expression. 
#It requires two parameters.
import re
re.findall("ts", "tsnow, tshah, bmoreno")
#The output is a list of only two elements, 
#the two matches to "ts": ['ts', 'ts'].
#to do more than search for specific strings, you must incorporate special symbols



###Regular expression symbols

#Symbols for character types
#\w matches with any alphanumeric character.
import re
re.findall("\w", "h32rb17")
#['h', '3', '2', 'r', 'b', '1', '7']

# . matches to all characters, including symbols
# \d matches to all single digits [0-9]
# \s matches to all single spaces 
# \. matches to the period character

import re
re.findall("\d", "h32rb17")
#['3', '2', '1', '7']

import re
re.findall("\.", "h32rb17")
#['h', '3', '2', 'r', 'b', '1', '7']

#Symbols to quantify occurrences
#Other symbols quantify the number of occurrences of a specific character in 
#the pattern. In a regular expression pattern, you can add them after a 
#character or a symbol identifying a character type to specify the number of 
#repetitions that match to the pattern.

#find more occurrences of a single digit
import re
re.findall("\d+", "h32rb17")
#['32', '17']
#the list contains the two matches of "32" and "17".

#* symbol
#The * symbol represents zero, one, or more occurrences of a specific character
import re
re.findall("\d*", "h32rb17")
#['', '32', '', '', '17', '']
#Because it also matches to zero occurrences, the list now contains empty 
#strings for the characters that were not single digits.
    
#If you want to indicate a specific number of repetitions to allow, you can place 
#this number in curly brackets ({ }) after the character or symbol. 
#In the following example, the regular expression pattern "\d{2}" instructs 
#Python to return all matches of exactly two single digits in a row from a 
#string of multiple device IDs:
import re
re.findall("\d{2}", "h32rb17 k825t0m c2994eh")
['32', '17', '82', '29', '94']
#Because it is matching to two repetitions, when Python encounters a single 
# digit, it checks whether there is another one following it. If there is, 
# Python adds the two digits to the list and goes on to the next digit. 
# If there isn't, it proceeds to the next digit without adding the first digit to the list.

#Python scans strings left-to-right when matching against a regular expression.
#When Python finds a part of the string that matches the first expected character
#defined in the regular expression, it continues to compare the subsequent characters
#to the expected pattern. When the pattern is complete, it starts this process again. 
#So in cases in which three digits appear in a row, it handles the third digit as a new starting digit.

#You can also specify a range within the curly brackets by separating two numbers with a comma. 
#The first number is the minimum number of repetitions and the second number is the maximum number of repetitions. 
#The following example returns all matches that have between one and three repetitions of a single digit:
import re
re.findall("\d{1,3}", "h32rb17 k825t0m c2994eh")
#['32', '17', '825', '0', '299', '4']


#Constructing a pattern
#Constructing a regular expression requires you to break down the pattern you're searching 
#for into smaller chunks and represent those chunks using the symbols 

#Your task is to extract the username and the login attempts, without the employee's ID number or department.
import re
pattern = "\w+:\s\d+"
employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
print(re.findall(pattern, employee_logins_string))
#['bmoreno: 12', 'tshah: 7', 'sgilmore: 5']
#The corresponding regular expression symbols are \w+, :, \s, and \d+ 
#respectively. Using these symbols as your regular expression,

#Exercise: using regular expressions in python 
#importing the re module.
import re
devices = "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u"
target_pattern = "r15\w+"
print(re.findall())
#\w matches with any alphanumeric character.
#+ matches with one or more occurrences of the character before it in the pattern.
#findall() function find the device IDs that start with "rt15"


#regular expression pattern to extract IP addresses
log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 192.168.190.178 \narutley 2022-05-12 17:00:59 1923.1689.3.24 \nrjensen 2022-05-11 0:59:26 192.168.213.128 \naestrada 2022-05-09 19:28:12 1924.1680.27.57 \nasundara 2022-05-11 18:38:07 192.168.96.200 \ndkot 2022-05-12 10:52:00 1921.168.1283.75 \nabernard 2022-05-12 23:38:46 19245.168.2345.49 \ncjackson 2022-05-12 19:36:42 192.168.247.153 \njclark 2022-05-10 10:48:02 192.168.174.117 \nalevitsk 2022-05-08 12:09:10 192.16874.1390.176 \njrafael 2022-05-10 22:40:01 192.168.148.115 \nyappiah 2022-05-12 10:37:22 192.168.103.10654 \ndaquino 2022-05-08 7:02:35 192.168.168.144"

pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

valid_ip_addresses = re.findall(pattern, log_file)

flagged_addresses = ["192.168.190.178", "192.168.96.200", "192.168.174.117", "192.168.168.144"]

for address in valid_ip_addresses:

    if address in flagged_addresses:
        print("The IP address", address, "has been flagged for further analysis.")
    else:
        print("The IP address", address, "does not require further analysis.")
#\d matches with digits, in other words, any integer between 0 and 9
#\. symbol matches with periods