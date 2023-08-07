#Automate cybersecurity tasks with python 
#Automating tasks in Python
#Automation is the use of technology to reduce human and manual effort to perform common and repetitive tasks.
#Automating cybersecurity-related tasks requires 
#understanding the following Python components:
#Variables
#Conditional statements
#Iterative statements
#Functions
#Techniques for working with strings
#Techniques for working with lists
#Working with files in Python

#Access a text file in Python
#importing a simple text file, restoring it as a string in Python
with open("name_of_text_file.txt", "r") as file:
#open files, read them
#open(function) - opens a file in python 
#"r" = second paramether == read a file 
#"w" = we could specify a second paramether as "w" which means write
#file = means file variable which is interconnected with "with" statement
#.read() method converts files into strings

with open("name_of_text_file.txt", "r") as file:
    file_text = file.read(name_of_the_text_file.txt)
    print(file_text)
#using read() function turns file into string, stores inside variable 

##Import files into Python
#Working with files in cybersecurity 
#Opening files in Python
#To open a file called "update_log.txt" in Python for purposes of reading it:
#with open("update_log.txt", "r") as file:
#it consists of the with keyword, the open() function with its two parameters, 
#and the as keyword followed by a variable name.

##with()
#The keyword with handles errors and manages external resources when used with other functions. 
#used with the open() function to open a file. It will then manage 
#the resources by closing the file after exiting the with statement.

##open()
#The open() function opens a file in Python.
#IF THE FILE WE WANT TO OPEN IS LOCATED IN THE SAME DIRECTORY AS PYTHON FILE THAT 
#WILL ACCESS IT, WE DONT HAVE TO SPECIFY PATH (otherwise there is specification needed)
#A file path is the location of a file or directory. An absolute file path starts from the 
#highest-level directory, the root. In the following code, 
#the first parameter of the open() function includes the absolute file path to "access_log.txt": 
with open("/home/analyst/logs/access_log.txt", "r") as file:
#In Python, the names of files or their file paths can be handled as string data, 
#and like all string data, you must place them in quotation marks

##as
#When you open a file using with open(), you must provide a variable that can store 
#the file while you are within the with statement. You can do this through the keyword 
#as followed by this variable name. The keyword as assigns a variable that references 
#another object. The code with open("update_log.txt", "r") as file: assigns file to 
#reference the output of the open() function within the indented code block that follows it.

##Reading files in Python
with open("update_log.txt", "r") as file:

    updates = file.read()

print(updates)
#The .read() method converts files into strings. 
#This is necessary in order to use and display the contents of the file
#the file variable is used to generate a string of the file contents through .read()
#This string is then stored in another variable called updates
#Once the file is read into the updates string, you can perform the same 
#operations on it that you might perform with any other string. 
#For example, you could use the .index() method to return the index where 
#a certain character or substring appears. Or, you could use 
#len() to return the length of this string.

##Writing files in Python
#To write to a file, you will need to open the file with "w" or "a" as the second argument of open()
#
#You should use the "w" argument when you want to replace the contents of an 
#existing file. When working with the existing file update_log.txt, 
#the code with open("update_log.txt", "w") as file: 
#opens it so that its contents can be replaced.
#
#Additionally, you can use the "w" argument to create a new file. 
#For example, with open("update_log2.txt", "w") as file: 
#creates and opens a new file called "update_log2.txt". 
#
#You should use the "a" argument if you want to append new information to the 
#end of an existing file rather than writing over it. 
#The code with open("update_log.txt", "a") as file: 
#opens "update_log.txt" so that new information can be appended to the end. 
#Its existing information will not be deleted.


##Parse a text file in Python
#Parsing
#is the process of converting data into a more readable format

#split() method
#converts a string into a list (separating the string based on a specified character)
#(if no argument is passed, every time it encounters a whitespace, it separates the string)
"We are learning about parsing!" #it converts it into this list:
["We", "are", "learning", "about", "parsing!"]


#previous file, open a file and print it into a string 
with open("name_of_text_file.txt", "r") as file:
    file_text = file.read(name_of_the_text_file.txt)
    print(file_text.split()) #using split() method 
#we now slip the string into a list using split() method 
usernames = file_text.split()
#we need to store the output into variable so we can use it in other code
#we store file_text.split() in usernames and store there output 

##Work with files in Python
#Parsing
#Parsing is the process of converting data into a more readable format
#Methods that can help you parse your data include .split() and .join()

#.split()
#The .split() method converts a string into a list
#It separates the string based on a specified character that's passed into .split() as an argument
approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
print("before .split():", approved_users) # elarson,bmoreno,tshah,sgilmore,eraab
approved_users = approved_users.split(",")
print("after .split():", approved_users) #['elarson', 'bmoreno', 'tshah', 'sgilmore', 'eraab']
#Before the .split() method is applied to approved_users, it contains a string,
#but after it is applied, this string is converted to a list.

#If you do not pass an argument into .split(), it will separate the string every time it encounters a whitespace.
removed_users = "wjaffrey jsoto abernard jhill awilliam"
print("before .split():", removed_users) #wjaffrey jsoto abernard jhill awilliam
removed_users = removed_users.split()
print("after .split():", removed_users) #['wjaffrey', 'jsoto', 'abernard', 'jhill', 'awilliam']

#Applying .split() to files
#The .split() method allows you to work with file content as a list after you've 
#converted it to a string through the .read() method. This is useful in a variety of ways. 
#For example, if you want to iterate through the file contents in a for loop, this can be 
#easily done when it's converted into a list.
with open("update_log.txt", "r") as file:
    updates = file.read()
updates = updates.split()
#Once a file is read into the updates variable, it is not needed and can be closed

#.join()
#if you need to convert a list into a string, there is also a method for that. 
#The .join() method concatenates the elements of an iterable into a string
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
print("before .join():", approved_users) #['elarson', 'bmoreno', 'tshah', 'sgilmore', 'eraab']
approved_users = ",".join(approved_users)
print("after .join():", approved_users) #elarson,bmoreno,tshah,sgilmore,eraab
#Before .join() is applied, approved_users is a list of five elements
#Another way to separate elements when using the .join() method is to use "\n", 
#which is the newline character. The "\n" character indicates to separate the 
#elements by placing them on new lines

#Applying .join() to files
#You might need to convert files back to strings from lists
with open("update_log.txt", "r") as file:
    updates = file.read()
updates = updates.split()
#After you're through performing operations using the list in the updates variable, 
#you might want to replace "update_log.txt" with the new contents. To do so, 
#you need to first convert updates back into a string using .join(). Then, 
#you can open the file using a with statement and use the .write() method to 
#write the updates string to the file
updates = " ".join(updates)
with open("update_log.txt", "w") as file
    file.write(updates)
#The code " ".join(updates) indicates to separate each of the list elements 
#in updates with a space once joined back into a string. And because "w" is 
#specified as the second argument of open(), Python will overwrite the 
#contents of "update_log.txt" with the string currently in the updates variable


#Activity: Import and parse a text file
#To analyze the security logs in these files, security analysts have to import and parse these files.
import_file = "login.txt"

with open(import_file, "r") as file: #import_file is saved as file on our system
    text = file.read()
print(file) #<_io.TextIOWrapper name='login.txt' mode='r' encoding='UTF-8'>


import_file = "login.txt"
with open(import_file, "r") as file:
  text = file.read()
# Display the contents of `text` split into separate lines 
print(text.split())
#['username,ip_address,time,date', 'tshah,192.168.92.147,15:26:08,2022-05-10', 
#'dtanaka,192.168.98.221,9:45:18,2022-05-09', 'tmitchel,192.168.110.131,14:13:41,2022-05-11',]


import_file = "login.txt"
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"
# Use `open()` to import security log file and store it as a string
# Pass in "a" as the second parameter to indicate that the file is being opened for appending purposes
with open(import_file, "a") as file:
    file.write(missing_entry)
with open(import_file, "r") as file:
    text = file.read()
print(text)


#There is a missing entry in the log file. You'll need to account for that by appending it to the log file. 
#You're given the missing entry stored in a variable named missing_entry.
import_file = "login.txt"

missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"

with open(import_file, "a") as file:
    file.write(missing_entry)
with open(import_file, "r") as file:
    text = file.read()
print(text)

#creating a text file
import_file = "allow_list.txt"
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"
print(import_file)
print(ip_addresses)
#read the file containing IP addresses
import_file = "allow_list.txt"
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"
with open(import_file, "w") as file:
    file.write(ip_addresses)
with open(import_file, "r")as file:
    text = file.read()
print(text)


#Develop a parsing algorithm
#program checking for certain username and if the username is 3 or more times the alert will be displayed
with open("login_attempts.txt", "r") as file:
    usernames = file_text.split()
    print(usernames) #shows contents of usernames (it is full of names)
#python checks and counts if the specified name is in the list 

def login_check(login_list, current_user):
    counter = 0
    for i in login_list:
        if i == current_user:
            counter = counter + 1
        if counter >= 3:
            return "You have tried to login three or more times. Your account has been locked"
        else:
            return: "You can log in!"
login_check(usernames, "eraab") #when we run our code and algorith
#we get an account locked message 



#Exercise
#Display both variables to explore their contents
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

print(import_file) #allow_list.txt
print(remove_list) #['192.168.97.225', '192.168.158.170', '192.168.201.40', '192.168.58.57']

#use the .read() method to read the imported file in as a string and store it in a variable named ip_addresses
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
with open(import_file, "r") as file:
  ip_addresses = file.read()

print(ip_addresses)#ip address ,192.168.25.60, 192.168.205.12, 192.168.97.225 ....

#reassign the ip_addresses variable so its data type is updated from a string to a list
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
with open(import_file, "r") as file:
    ip_addresses = file.read()
ip_addresses = ip_addresses.split() #.split method changes data type from string to a list 
print(ip_addresses)


#write code that removes the elements of remove_list from the ip_addresses list
# Build `with` statement to rewrite the original file
# Define a function named `update_file` that takes in two parameters: `import_file` and `remove_list`

#loop variable = (typically) i, in this exercise = element
#.remove() method deletes only first occurence of an element in the file 
# Define a function named `update_file` that takes in two parameters: `import_file` and `remove_list`
def update_file(import_file, remove_list)
    with open(import_file, "r") as file: #imports file as read
       
        ip_addresses = file.read()       #we read imported file and store it in ip_addresses variable 
        
    ip_addresses = ip_addresses.split() #.split() converts string to a list 

    for element in remove_list: #build an itertarive statement
        if element in ip_addresses: #if element is in ip addresses
            ip_addresses.remove(element) #.remove method to remove elements from ip_addresses

    ip_addresses = "\n".join(ip_addresses) #converts ip_addresses back to a string from list 

    with open(import_file, "w") as file: #rewriting the original file 

        file.write(ip_addresses)


##########################################################################
#Python file algorithm TEST

#Update a file through a Python algorithm
#Access to organization, the "allow_list.txt" file identifies these IP addresses
import_file = "allow_list.txt"

with open(import_file, "r") as file:
    ip_addresses = file.read()

    ip_addresses = ip_addresses.split()

    for element in remove_list: #iterating throught remove list 
        if element in ip_addresses:
            ip_addresses.remove(element)

            ip_addresses = "\n".join(ip_addresses)

            with open(import_file, "w") as file:
                file.write(ip_addresses)
#I created an algorithm that removes IP addresses identified in a remove_list 
#variable from the "allow_list.txt" file of approved IP addresses. 
#This algorithm involved opening the file, converting it to a string to be read,
#and then converting this string to a list stored in the variable ip_addresses.
#I then iterated through the IP addresses in remove_list. With each iteration, 
#I evaluated if the element was part of the ip_addresses list. If it was, 
#I applied the .remove() method to it to remove the element from ip_addresses..
#After this, I used the .join() method to convert the ip_addresses back into a 
#string so that I could write over the contents of the "allow_list.txt" file 
#with the revised list of IP addresses.
