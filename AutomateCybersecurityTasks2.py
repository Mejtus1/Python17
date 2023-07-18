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

