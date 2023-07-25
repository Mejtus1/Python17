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

