# Create a Basic Python script 
# Hashes are used in python for comments 

#print - outputs a specified object to a screen 
print("Hello, Python")


#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#DATA TYPES IN PYTHON 

#Strings 
#Data consisting of an ordered sequence of characters
#letters, symbols, spaces or numbers (numbers cannot be used in calculations)
#strings need to be inside quoation marks ""
print("hello python")

#Float data
#Data consisting of a number with a decimal point 
# 2.1 10.1 10.00

#Integer data 
#data consisting of a number that does not include a decimal point 
# 1, 48 , 12478514

print(1 + 1)#calcualtion with print 

#boolean data
#Data that cen only be one of two values - true or false
print(10<5)
print(9<12) #Determine boolean values 

#List Data
#Data structure that consists of a collection of data in sequantial form 
print(["dtanaka", "mabadi", "aestrada"]) #(like arrays in JS)


#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
# Work with variables in python 
# creating variables is called assigment 
# we can reassign a variable whenever we want 
device_id = "hb2r17"
device_id = "145236hre" #reassign
print(device_id)
#we can ask python to tell us a data type of our variable
data_type = type(device_id)
print(data_type) #python tells us it is a string (str)

#Type error 
#an error that results from using the wrong data type 
number = 3
print(number + device_id) #throws type error
#python cannot combine two different data types

#Exercises
device_id = "72e08x0"
print(device_id)

# Assign the `device_id` variable to the device ID that only specified users can access
device_id = "72e08x0"
# Assign `device_id_type` to the data type of `device_id`
device_id_type = type(device_id)
# Display `device_id_type`
print(device_id_type)
    
# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
# Display `username_list`
print(username_list)

# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
# Assign `username_list_type` to the data type of `username_list`
username_list_type = type(username_list)
# Display `username_list_type`
print(username_list_type)

# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
# Display `username_list`
print(username_list)

# Assign `max_logins` to the value 3
max_logins = 3
# Assign `max_logins_type` to the data type of `max_logins`
max_logins_type = type(max_logins)
# Display `max_logins_type`
print(max_logins_type)

# Assign `login_attempts` to the value 
login_attempts = 2
# Assign `login_attempts_type` to the data type of `login_attempts`
login_attempts_type = type(login_attempts)
# Display `login_attempts_type`
print(login_attempts)
# Assign `login_status` to the Boolean value False
login_status = 5
# Assign `login_status_type` to the data type of `login_status`
login_status_type = type(login_status)
# Display `login_status_type`
print(login_status_type)


#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#Conditional statements in python 
#A statement that evaulates code to determine if it meets a specified set of conditions
#"if" starts a conditional statement 
if failed_attempts > 5:
    print("Account locked")

#operators = > < >= <= == != 
operating_system = "OS 2"
if operating_system == "OS 2":
    print("Updates needed")

#else
#precedes a code section that only evaluates when all conditions that precede
#within the conditional statement evaluate to False

operating_system2 = "OS 2"
operating_system3 = "OS 3"
if operating_system3 == "OS 2": # dont forget :
    print("updates needed")
else:
    print("No updates needed")

#other examples

status = "check other status":
if status == 200:
    print("OK")
else:
    print("check other status")

#HTTP response python example 
if status == 200:
    print("OK")
elif status == 400:
    print("Bad Request")
elif status == 500:
    print("Internal Server Error") 


#AND in python 
#and operator requires both conditions to be true 
#HTTP example 
if status >= 200 and status <= 226: #HTTP responses between 200 and 226 are successful
    print("successful response")

#OR operator in python 
#OR operator requires only one condition to be true 
#HTTP example
#both 100 and 102 are informal responses 
if status == 100 or status == 102:
    print("informational response")

#NOT operator in python 
#NOT operator negates the given condition so that it evaulates to false
if not(status >= 200 and status <= 226):
    print("check status") #checking when something is out of succesful code

#Exercises
system = "OS 2"
if ("OS 2"):
    print("no update needed")

system2 = "OS 1"
if system2 == "OS 2":
    print("no update needed")
else:
    print("update needed")

system3 = "1"
if system3 == "OS 2":
    print("no update needed")
elif system3 == "OS 1":
    print("update needed")
elif system3 == "OS 3":
    print("update needed")


system4 = "OS 2"
if system4 == "OS 1":
    print("no update needed")
elif system4 == "OS 2" or "OS 3":
    print("update needed")


approved_user1 = "elarson"
approved_user2 = "bmoreno"
username = "bmoreno"
if user == approved_user1 or approved_user2:
    print("This user has access to this device.")
else
    print("This user does not have access to this device.")


approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
username = "bmoreno"
if username in approved_list:
    print("approved")
else:
    print("You do not have access to this device")

#Main exercise
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
username = "bmoreno"
if username in approved_list:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")
organization_hours = True
if organization_hours == True:
    print("Login attempt made during organization hours.")
else:
    print("Login attempt made outside of organization hours.")

#Main exercise2 (using and)
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
username = "bmoreno"
organization_hours = True
if username in approved_list and organization_hours == True:
    print("Login attempt made by an approved user during organization hours.")
else:
    print("Username not approved or login attempt made outside of organization hours.")
    


#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#For loops 
#Iterative statement = code that repeatedly executes a set of instructions (loops)
#they allow us to repeatedly use a line of code without having to type it multiple times
for i in [1,2,3,4]:
    print(i)
#for starts a statement 
# i = loop variable, is used to control iterations fo a loop 
# in [1,2,3,4] (list) 
range(0,10) # range specifies sequence 
range(10)   # if we dont provide start point for range it automatically starts from 0

for i in range(10):
    print("Cannot connect to the destination.") #python writes it 10 times


#While loops 
#while loops still repeatedly execute, but this repetition is based on condition
#as long as a condition is true it runs)
max_devices =5
i = 1
while i < max_devices:
    print("User can still connect to additional devices")
    i = i + 1 #we increment i by 1 
print("User has reached maximum number of connected devices") #outside of the loop

#more on loops in python
#iterative statement is a code that repeatedly executes a set of instructions (for loops are used to loop over a sequence)
#for loop
#if you need to iterate through a specified sequence, you should use a for loop
for i in ["elarson", "bmonero", "tsash", "sigilmore"]:
  print(i)
#the : must be at the end of each for loop header
#this is example of loop where in operator is used to loop over a sequence

if "elarson" in ["elarson", "bmonero", "tsash", "sigilmore"]
#this is example of in used: in conditional state - evaulate if an object is part of an object sequence
#evaulates to true

#Looping through a list
#for loops in python allow you to easily iterate throught list
#example: asset is a loop variable and computer_assets is the sequence
computer_assets = ["laptop01", "desktop13", "smartphone17", "laptop07"]
for asset in computer_assets:
  print(character)
#first iteration = output("laptop01")

#it is also possible to iterate through string
string = "security"
for character in string:
  print(character)

#using range()
#the range function generates a sequence of numbers
#it accepts: start point, stop point, increment

range (0, 5, 1)
#start sequence of numbers at 0, stop at 5, increment by 1

for i in range(0, 5, 1):
  print(i)
#5 is excluded from this range 0-4 is outputted

#start and stop point should be always included into the function code
#exception is start of 0 and increment by 1
for i in range(5):
  print(i)
#otherwise they should be specified

#while loops
#loops based on condition
#as long as the condition is true, the loop continues until the condition is false
i = 1
while i < 5:
  print(i)
  i = i + 1
# i is assigned before loop header
# body indicates the actions to take with each iteration

#integers in loop condition
#Often, as just demonstrated, the loop condition is based on integer values. 

#For example you might want to allow a user to log in as long as they've logged in less than five times. 
#Then, your loop variable, login_attempts, can be initialized to 0, incremented by 1 in the loop, and the loop condition can specify to iterate only when the variable is less than 5.
login_attempts = 0
while login attempts < 5:                 
    print("Login attempts:", login attempts)
login attempts login_attempts + 1
#The value of login attempts went from 0 to 4 before the loop condition evaluated to False. Therefore, the values of 0 through 4 print, and the value 5 does not print.

#Boolean values in the loop condition
#Conditions in while loops can also depend on other data types, including comparisons 
#of Boolean data in Boolean data comparisons, your loop condition can check whether 
#a loop variable equals a value like True or False. 
#The loop iterates an indeterminate number of times until the Boolean condition is no longer True

#Boolean values in the loop condition
count = 0
login_status = True
while login_status == True:
    print("Try again.")
    count = count + 1
    if count == 4:
        login_status = False
#while only iterates when login_status is True

#managing loops 
#you can use break and continue keywords to further control you loop iterations

#break
#it is used when you want to exit a for or while loop based on particular condition
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        break #using break in the code
    print(asset)
#values of desktop20 and smartphone03 dont print 

#continue
#is used to skip iteration over certain element
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        continue #using continue to skip over desktop asset
    print(asset)

#in infinite loop scenario you sould press CTRL-C or CTRL-Z 



#exercises
for i in range(0, 3, 1):
    print("Connection could not be established.")

#we can also use a variable in range() function 
connection_attempts = 3
for i in range(0, connection_attempts, 1):
    print("Connection could not be established")

#while loop
while connection_attemps == 3:
    print("Connection could not be established.")
    connection_attempts = connection_attempts + 1


#automate checking whether IP addresses are part of an allow list.
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

for i in ip_addresses:
    print(i)


#IP ADDRESS check list using for and if 
allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]
# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
for i in ip_addresses:
	if i in allow_list:
		print("IP address is allowed")
	else:
		print("IP address is not allowed")
                

#break using loops 
allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]
# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
for i in ip_addresses:
	if i in allow_list:
		print("IP address is allowed")
    else) 
        print("IP address is not allowed")
        #break 

#creating IDs numbers between 5000 and 5150
i = 5000
while i <= 5150: 
    print(i)
    i += 5

i = 5000

#creating IDs with text if only 10 are remaining
while i <= 5150: 
    print(i)
    if i == 5100:
        print("only 10 valid IDs remaining")
    i = i + 5


