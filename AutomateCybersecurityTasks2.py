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
