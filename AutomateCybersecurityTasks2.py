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
