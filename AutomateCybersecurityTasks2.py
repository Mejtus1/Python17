#Functions 
#using for reusing same lines of code 
#it is a section of code that can be reused in a program 

#def is placed before a functin name to define a function
def
#we define a functin 
def greet_employee():
    print("Welcome! You are logged in.")
    #call a function 
greet_employee()


#more complex function 
def display_investigation_message():
    print("investigate activity")
application_status = "potential concern"
email_status = "okay"
if application_status == "potential concern":
    print("application_log:")
    display_investigation_message()
if email_status == "potential concern":
    print("email log:")
    display_investigation_message()


#python functions exercises
def alert():
    print("Potential security issue. Investigate further.")

#function using for loops 
def alert1(): 
    for i in range(3):
        print("Potential security issue. Investigate further.")
alert1()

#Main Exercise
#developing a function with a list of approved usernames
def list_to_string():

username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

sum_variable = ""

for i in username_list:
    sum_variable = sum_variable + i + ", "
    print(sum_variable)

list_to_string()


#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#USE paramethers inside a functions 
#Paramether is an object that is included inside a function in use for that function 
# -//- are accepted into a function throught a parenthesis after a function name 
range(start, stop) # start and stop values are range function paramethers
range(3, 7) #the sequence it generates will run from 3 to 6

#greet employees by name paramether
def greet_employee(name):
    print("Welcome! You are logged in", name)
#name is here a paramether defined in our function, and we want to use it when function is invoked

#Argument is a data brought into a function when it is called
greet_employee("Vicky") #Vicky is an argument 


#more paramethers and arguments inside a functions 
def greet_employee2(first_name2, last_name2):
    print("Welcome! You are logged in", first_name2, last_name2)

greet_employee2("Vicky", "Jack")


#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#Return statements
#a python statement that executes inside a function and sends information back to the function call

def calculate_fails(total_attempts, failed_attempts):
    fail_percentage = failed_attempts / total_attempts
    return fail_percentage

calculate_fails(4,2)
#fail_percentage cannot be used outside of the scope of the function 
#for that we need to store output of our function in another variable 
percentage = calculate_false(4,2)

if (percentage >= .5):
    print("Account locked")

#if the percentage is higher than 50% (0.5) then the account is locked



#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#Global and local variables
#When defining and calling functions, you're working with local variables
#A global variable is a variable that is available through the entire program. 
#Global variables are assigned outside of a function definition.

#For example, you might assign the following variable at the beginning of your code:
device_id = "7ad2130bd

#Local variable 
def greet_employee(name):           #name is a local variable
    total_string = "Welcome" + name #total_string is a local variable
    return total_string
#The variable total_string is a local variable because it's assigned inside of the function. 
#The parameter name is a local variable because it is also created when the function is defined. 


#Best practices for using LOCAL and GLOBAL variables
#it is very important to make sure that you only use a certain variable name once, 
#even if one is defined globally and the other is defined locally. 
username = "elarson"
def identify_user():
    print(username)
identify_user()
#function can access username elarson even when it is outside of its scope, because it is globally assigned

#scopes
username = "elarson" #global variable
print("1:" + username)
def greet():
    username = "bmoreno" #we reeasign variable here, and it becomes local 
    print("2:" + username) #so reeasigned variable username is now inside function
greet()                    #bmoreno BUT OUTSIDE FUNCTION IS STILL elarson 
print("3:" + username)     #the username variable doesnt change on global scale




#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#Build in functions 
#are functions that exist within python and can be called directrly
#we already know 
print() #outputs a specified obejct to the screen
type() #returns a data type of its input

#we can pass one functino into another as an argument
print(type("Hello")) #outputs string 

#explore input and output of print() function 
print("This is a string, but", 75, "is a number.")

#max function
a = 3
b = 9 
c = 6
print(max(a,b,c)) #it tells us the highest number of specified arguments

#sorted()
#sorts a components of a list
usernames = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
print(sorted(usernames))
#when we run it everything is in order


#Exploring types of build in functions 
#print() 
#The print() function outputs a specified object to the screen.
month = "September"
print("Investigate failed login attempts during", month, "if more than", 100)

#type()
#The type() function returns the data type of its argument. 
#The type() function helps you keep track of the data types of variables to avoid errors throughout your code. 
type("security")

#Passing one function into another
#When working with functions, you often need to pass them through print() 
#if you want to output the data type to the screen.
print(type("This is a string"))

#max() and min() 
#The max() function returns the largest numeric input passed into it. 
#The min() function returns the smallest numeric input passed into it.
#n a cybersecurity context, you could use these functions to identify 
#the longest or shortest session that a user logged in for.
time_list = [12, 2, 32, 19, 57, 22, 14]
print(min(time_list))
print(max(time_list))

#sorted()
#The sorted() function sorts the components of a list. 
#The sorted() function also works on any iterable, like a string, and returns the sorted elements in a list.
time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))
print(time_list)


#more on python build in functions (activity with code)
#sorting months 
failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]
print(sorted(failed_login_listlogin_list))

#printing out highest number of infcidents month
failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]
print(max(failed_login_list))

#program for loggin analysis and warning when certain condition is met 
def analyze_logins(username, current_day_logins, average_day_logins):
    print("Current day login total for", username, "is", current_day_logins)
    print("Average logins per day for", username, "is", average_day_logins)
    login_ratio = current_day_logins / average_day_logins
    return login_ratio

login_analysis = analyze_logins("ejones", 9, 3)
if login_analysis >= 3:
    print("Alert! This account has more login activity than normal.")




#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#Modules and libraries
# a library is a collection of modules that provide code users can access in their programs
# all libraries are generally made of multiple modules
# a module is a python file that contains additional functions, variables,
# classes and any kind of runnable code

#Python Standard Library
# is an extensive collection of usable code that comes packaged with python 
# useful module is "re" module
# another one is "csv" module
# glob, os, time, datetime

#external libraries can also be downloaded 
#Beautiful Soup = parsing HTML website files
#NumPx = for arrays and mathematical computations


#Import modules and libraries in Python 
#module is a Python file that contains additional functions, variables, classes, and any kind of runnable code
#library is a collection of modules that provide code users can access in their programs.

#The "re" module, which provides functions used for searching for patterns in log files
#The "csv" module, which provides functions used when working with .csv files
#The "glob" and os modules, which provide functions used when interacting with the command line
#The "time" and datetime modules, which provide functions used when working with timestamps
#The mean() and median() are statistical functions from module statistics


#How to import modules from the Python Standard Library
#To access modules from the Python Standard Library, you need to import them. 
#You can choose to either import a full module or to only import specific functions from a module. 

#Importing an entire module
#import keyword searches for a module or library in a system and adds it to the local Python environment

#For example, you can specify import statistics to import the statistics module.
#As an example, you might want to use the mean() function from the statistics module 
#to calculate the average number of failed login attempts per month for a particular user.
import statistics
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
mean_failed_attempts = statistics.mean(monthly_failed_attempts)
print("mean:", mean_failed_attempts) #mean = 35.25
print("median:", median_failed_attempts) #median = 20.5
#we used statistics.mean() and statistics.meidan() functions in our program which we imported

#Importing specific functions from a module
#To import a specific function from the Python Standard Library, you can use the from keyword. 
#For example, if you want to import just the median() function from the statistics module, 
#you can write from statistics import median.
#from statistics import mean, median #this is how we import more specific functions 
from statistics import mean, median
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
mean_failed_attempts = mean(monthly_failed_attempts)
print("mean:", mean_failed_attempts)
median_failed_attempts = median(monthly_failed_attempts)
print("median:", median_failed_attempts) 

#External libraries
#In addition to the Python Standard Library, you can also download external libraries
#Beautiful Soup (bs4) for parsing HTML files 
#NumPy (numpy) for arrays and mathematical computations.
%pip install numpy #installs the library
#After a library is installed, you can import it directly into Python using the import keyword
import numpy #we use import numpy 

