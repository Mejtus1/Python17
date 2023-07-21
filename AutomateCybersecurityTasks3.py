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
