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

#with()
#The keyword with handles errors and manages external resources when used with other functions. 
#used with the open() function to open a file. It will then manage 
#the resources by closing the file after exiting the with statement.

