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
